import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def classify_threat(message):
    prompt = f"Classify the following message as either 'phishing', 'malware', 'harmless', or 'suspicious'. Provide only the label.\nMessage: {message}"
    response = genai.GenerativeModel('gemini-pro').generate_content(prompt)
    return response.text.strip()

def detect_phishing(message):
    prompt = f"Is the following message a phishing attempt? Respond with 'Yes' or 'No' and explain briefly why.\nMessage: {message}"
    response = genai.GenerativeModel('gemini-pro').generate_content(prompt)
    return response.text.strip()

def summarize_incident(text):
    prompt = f"Summarize the following security report or incident in simple terms:\n{text}"
    response = genai.GenerativeModel('gemini-pro').generate_content(prompt)
    return response.text.strip()
