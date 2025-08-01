# 🧠 Report Generator Bot

This is a lightweight AI-powered Python script that fetches student quiz data from Google Sheets (submitted via a Google Form), generates personalized feedback using Together AI's language models, and outputs a clean PDF report for each student.

---

## 🚀 Features

- 🔗 Google Sheets integration
- 🤖 AI-generated student feedback using Together.ai
- 📄 PDF report generation
- 📥 All reports saved locally
- ⚙️ Simple and reproducible setup using `uv`

---

## 📁 Project Structure

Report-generator-bot/
├── .env # Environment config
├── creds.json # Google Cloud service account credentials
├── main.py # Main runner script
├── pyproject.toml # Project dependency file
├── uv.lock # Lockfile for uv
├── reports/ # Output folder for PDFs
├── README.md
└── utils/
├── llm_handler.py # Handles Together AI API
├── report_writer.py # Generates feedback and PDF
└── sheet_handler.py # Fetches data from Google Sheets


---

## ⚙️ Setup Instructions

### ✅ 1. Google Cloud Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or use an existing one
3. **Enable APIs**:
   - Google Sheets API
   - Google Drive API
4. **Create a Service Account**:
   - Go to `APIs & Services > Credentials`
   - Create a Service Account with **Editor** access
   - Under "Keys", click `Add Key > Create new key > JSON`
   - Download and rename the file to `creds.json`, and place it in your root directory
5. **Share your Google Sheet**:
   - Open your sheet
   - Share it with the email inside your `creds.json` file

---

### 📋 2. Google Form + Sheet

- Create a Google Form with fields like:
  - `Student Name`
  - `Email ID`
  - `Math Score`
  - `English Score`
  - `Science Score`
- Link it to a Google Sheet automatically (it usually ends in `"(Responses)"`)
- Copy that sheet name for the `.env` file

---

### 🤖 3. Together AI Setup

1. Go to [https://www.together.ai](https://www.together.ai)
2. Sign up and get your **API Key** (`tgp_v1_...`)
3. Choose a free supported model like:
   - `mistralai/Mistral-7B-Instruct-v0.1`
   - `Qwen/Qwen1.5-0.5B-Chat` (if Mistral is unavailable)
4. No need to host anything — Together provides serverless inference!

---

### 📄 4. Create `.env` File

Create a `.env` file in the root directory:

```env
GOOGLE_SERVICE_ACCOUNT_FILE=creds.json
GOOGLE_SHEET_NAME=Student_Quiz_Submission_(Responses)
TOGETHER_API_KEY=tgp_v1_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TOGETHER_MODEL=mistralai/Mistral-7B-Instruct-v0.1
📦 5. Install Dependencies using uv
Make sure uv is installed:


curl -Ls https://astral.sh/uv/install.sh | sh
Then install dependencies:


uv venv
uv pip install python-dotenv gspread oauth2client fpdf requests
▶️ How to Run
Just execute:


python main.py
You'll see logs like:


📄 Fetching student records from sheet: Student_Quiz_Submission_(Responses)
✅ Found 1 student records.

➡️ Processing student 1: Aamir
   ✅ PDF generated at: reports/aamir_report.pdf
📂 Sample PDF Output
Each student gets a file like:


reports/aamir_report.pdf
PDF contains:

Name & Email

Subject-wise scores

Personalized AI feedback (one short paragraph)

🔍 Example Prompt Sent to LLM

Generate a short, friendly feedback report for the following student:

Name: Aamir
Email: aamir@example.com
Math Score: 85/100
English Score: 74/100
Science Score: 92/100

Give clear strengths and one or two areas of improvement. Be positive and helpful.
🛠️ Debug Tips
Make sure all sheet columns match exactly (Email ID, not Email ID with trailing space)

Update .env if the sheet name or API key changes

If the model throws model_not_available, try switching to another supported model

✅ Next Improvements
Send reports via email using Gmail API

Log feedback into a new sheet tab

Web-based interface (Flask/Streamlit)

Automatic run on new submissions (via Apps Script or cron)










