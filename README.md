# 🏗️ Project Swaraj – AI Site Progress Assistant
<p align="center">
  <img src="images/Banner.png" alt="Project Swaraj Banner" width="100%">
</p>

An AI-powered construction site reporting system built using **Google Gemini** and **Python**.

The system converts a worker's voice note into structured project updates and automatically records them in a Google Sheet.

---

## 🚀 Problem Statement

Construction supervisors often receive daily updates through phone calls or voice notes. These updates are:

- Unstructured
- Time-consuming to document
- Difficult to track consistently

This project automates that entire workflow.

---

## ✨ Features

- 🎤 Accepts worker voice notes (.ogg)
- 📝 Transcribes speech into text using Google Gemini
- 🤖 Extracts structured project information using AI
- 📊 Automatically updates Google Sheets
- 📅 Records timestamp and reporting date
- ⚠️ Captures issues and material requirements
- 👷 Identifies worker information
- 📋 Generates structured daily site reports

---

## 🏛️ Architecture

```
Worker Voice Note (.ogg)
            │
            ▼
 Google Gemini Transcription
            │
            ▼
 Structured JSON Extraction
            │
            ▼
 Google Sheets Update
```

---

## 📂 Project Structure

```
Swaraj_AI_ADK/
│
├── data/
│   └── worker_voice.ogg
│
├── siteops/
│   ├── progress_agent.py
│   ├── summary_agent.py
│   ├── siteops_agent.py
│   └── workflows/
│
├── run_project.py
├── transcribe_audio.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Tech Stack

- Python
- Google Gemini API
- Google Sheets API
- gspread
- python-dotenv

---

## ▶️ How to Run

1. Clone the repository

```
git clone <repository-url>
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Add your Google API Key inside a `.env` file

```
GOOGLE_API_KEY=YOUR_API_KEY
```

4. Add your Google Service Account credentials as `credentials.json`.

5. Place your worker voice note inside:

```
data/worker_voice.ogg
```

6. Run

```
python run_project.py
```

---

## 📈 Sample Output

The system extracts:

- Worker Name
- Date
- Site
- Completed Work
- Next Planned Work
- Issues
- Materials Required

and automatically updates a Google Sheet.

---

## 🔮 Future Improvements

- WhatsApp integration
- Telegram Bot integration
- Multi-worker reporting
- Automatic PDF report generation
- Supervisor dashboard
- Daily email summaries

---

## 👩‍💻 Developed By

**Shweta Goswami**

AI Site Progress Assistant – Capstone Project
