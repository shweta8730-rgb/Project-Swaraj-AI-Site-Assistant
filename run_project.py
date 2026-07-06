import os
import json
from datetime import datetime

import gspread
from dotenv import load_dotenv
from google import genai
from google.oauth2.service_account import Credentials

from transcribe_audio import transcribe_audio

# -----------------------------
# Load Gemini API Key
# -----------------------------
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# -----------------------------
# Step 1: Transcribe Audio
# -----------------------------
transcribed_text = transcribe_audio("data/worker_voice.ogg")

print("\n========== TRANSCRIPTION ==========")
print(transcribed_text)
print("===================================\n")

# -----------------------------
# Step 2: Extract Structured JSON
# -----------------------------
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"""
You are an AI Site Progress Engineer.

Analyze the following construction site update and return ONLY valid JSON.

IMPORTANT:
- Do NOT guess or infer any information.
- If the worker does NOT mention the site/location, leave "site_name" as an empty string.
- If the worker does NOT mention the date, leave "date" as an empty string.

Use this format:

{{
  "worker_name": "",
  "site_name": "",
  "date": "",
  "completed_work": [],
  "next_planned_work": [],
  "issues": [
    {{
      "issue": "",
      "severity": "Low | Medium | High"
    }}
  ],
  "materials_required": [
    {{
      "material": "",
      "quantity": "",
      "unit": ""
    }}
  ]
}}

Construction Site Update:

{transcribed_text}
"""
)

clean_json = (
    response.text
    .replace("```json", "")
    .replace("```", "")
    .strip()
)

json_data = json.loads(clean_json)

# Fill today's date only if Gemini leaves it blank
if not json_data["date"]:
    json_data["date"] = datetime.now().strftime("%d %B %Y")

# Current timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("========== EXTRACTED JSON ==========")
print(json.dumps(json_data, indent=2))
print("====================================\n")

# -----------------------------
# Step 3: Google Sheets
# -----------------------------
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES
)

gc = gspread.authorize(creds)

sheet = gc.open("Project Swaraj - Daily Progress").sheet1

completed_work = "\n".join(json_data["completed_work"])

next_work = "\n".join(json_data["next_planned_work"])

issues = "\n".join(
    issue["issue"]
    for issue in json_data["issues"]
)

materials = "\n".join(
    f'{m["quantity"]} {m["unit"]} {m["material"]}'.strip()
    for m in json_data["materials_required"]
)

sheet.append_row([
    timestamp,
    json_data["date"],
    json_data["site_name"],       # Blank if not mentioned
    json_data["worker_name"],
    completed_work,
    next_work,
    issues,
    materials,
    "",
    ""
])

print("✅ Google Sheet updated successfully!")