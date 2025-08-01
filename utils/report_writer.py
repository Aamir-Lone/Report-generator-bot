from typing import Dict
from fpdf import FPDF
import os
from utils.llm_handler import query_llm


def generate_feedback(student_data: Dict[str, str]) -> str:
    name = student_data.get("Student Name", "Unknown")
    email = student_data.get("Email ID", "N/A")
    math = student_data.get("Math Score", "0")
    english = student_data.get("English Score", "0")
    science = student_data.get("Science Score", "0")

    prompt = f"""
Generate a short, friendly feedback report for the following student:

Name: {name}
Email: {email}
Math Score: {math}/100
English Score: {english}/100
Science Score: {science}/100

Give clear strengths and one or two areas of improvement. Be positive and helpful.
"""

    return query_llm(prompt)


def generate_pdf(student_data: Dict[str, str], feedback: str, output_dir: str = "reports") -> str:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = f"{student_data.get('Student Name', 'student').replace(' ', '_')}_report.pdf"
    filepath = os.path.join(output_dir, filename)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Student Performance Report", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Name: {student_data.get('Student Name', 'Unknown')}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {student_data.get('Email ID', 'N/A')}", ln=True)
    pdf.cell(200, 10, txt=f"Math Score: {student_data.get('Math Score', '0')}/100", ln=True)
    pdf.cell(200, 10, txt=f"English Score: {student_data.get('English Score', '0')}/100", ln=True)
    pdf.cell(200, 10, txt=f"Science Score: {student_data.get('Science Score', '0')}/100", ln=True)
    pdf.ln(10)

    pdf.multi_cell(0, 10, txt="Feedback:\n" + feedback)

    pdf.output(filepath)
    return filepath


