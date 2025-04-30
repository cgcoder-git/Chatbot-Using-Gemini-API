from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from openai_constants import GEMINI_API_KEY
import re



app = Flask(__name__)

# Configure Gemini API
API_KEY = os.environ.get("GEMINI_API_KEY") or GEMINI_API_KEY
genai.configure(api_key=API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

# Store chat history in memory
chat_history = []

# This function will extract Hindi text from the input
def extract_hindi(text):
    # This regex will keep only Devanagari characters and spaces
    hindi_text = re.findall(r'[\u0900-\u097F\s]+', text)
    return ''.join(hindi_text).strip()

def chat_with_gemini(prompt):
    updated_prompt = f"user asked {prompt}, please reply users question's answer only in chhattishgarhi language and use hindi script"
    try:
        response = model.generate_content(updated_prompt)
        reply_text = response.text.strip()
        hindi_only = extract_hindi(reply_text)
        print("Chhatishgardhiya Gemini:", hindi_only)
        return hindi_only
    except Exception as e:
        return f"Error: {e}"
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    user_input = data.get("message", "").strip()
    if not user_input:
        return jsonify({"response": "Please enter a message."})

    # Add user input to history
    chat_history.append({"role": "user", "message": user_input})

    # Get Gemini response
    gemini_response = chat_with_gemini(user_input)
    chat_history.append({"role": "gemini", "message": gemini_response})

    return jsonify({"response": gemini_response})

if __name__ == "__main__":
    app.run(debug=True)
