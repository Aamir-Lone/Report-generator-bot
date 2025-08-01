import os
from dotenv import load_dotenv
from utils.sheet_handler import get_sheet_records
from utils.report_writer import generate_feedback, generate_pdf

def main():
    load_dotenv()

    SHEET_NAME = os.getenv("GOOGLE_SHEET_NAME")
    if not SHEET_NAME:
        raise ValueError("GOOGLE_SHEET_NAME not set in .env file.")

    print(f"Fetching student records from sheet: {SHEET_NAME}")
    students = get_sheet_records(SHEET_NAME)

    if not students:
        print("No student data found.")
        return

    print(f"Found {len(students)} student records.\n")

    for i, student in enumerate(students, start=1):
        print(f"Processing student {i}: {student['Student Name']}")
        # print("Fields:", student.keys())#for debugging


        try:
            feedback = generate_feedback(student)
            pdf_path = generate_pdf(student, feedback)
            print(f"PDF generated at: {pdf_path}")
        except Exception as e:
            print(f"Failed to process {student['Student Name']}: {e}")

if __name__ == "__main__":
    main()



