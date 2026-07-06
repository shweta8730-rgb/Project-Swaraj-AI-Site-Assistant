import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def transcribe_audio(audio_path):
    audio_file = client.files.upload(
        file=audio_path
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            "Transcribe this construction site voice note into plain English.",
            audio_file
        ]
    )

    return response.text