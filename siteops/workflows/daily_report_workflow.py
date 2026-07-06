import gspread
from google.oauth2.service_account import Credentials

# Google API scope
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Authenticate
creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("Project Swaraj - Daily Progress").sheet1

# Test row
sheet.append_row([
    "2026-06-30 10:30",
    "30 June 2026",
    "Verna",
    "Ramesh",
    "Completed brick wall",
    "Start plastering",
    "One labourer absent",
    "20 bags cement",
    "",
    "",
    "",
    "",
    "• Completed brick wall\n• Labour shortage\n• Cement required"
])

print("✅ Row added successfully!")