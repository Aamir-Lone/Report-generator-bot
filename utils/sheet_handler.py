from typing import List, Dict
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

# Define the Google Sheets scope
SCOPES = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

def get_sheet_records(sheet_name: str) -> List[Dict[str, str]]:
    # Load service account credentials
    creds_path = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")
    if not creds_path:
        raise ValueError("GOOGLE_SERVICE_ACCOUNT_FILE not set in environment.")

    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, SCOPES)

    # Authorize and open the sheet
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1  # Opens the first worksheet
    records = sheet.get_all_records()

    return records
