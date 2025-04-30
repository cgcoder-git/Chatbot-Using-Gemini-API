# Chatbot-Using-Gemini-API
lets learn about how to make chatbot using gemini api

## What is API ?
**API** stands for **Application Programming Interface**. It’s a software bridge that allows two applications to communicate with each other. APIs make it easy to access and share data across systems, apps, and even organizations.

### APIs are everywhere — whether you’re:

* Booking a cab through a rideshare app,
* Sending money via mobile payment,
* Or adjusting your home’s thermostat from your phone.
Each of these actions uses an API behind the scenes.

## Create a Chatbot with Gemini API :
We need to follow the below step to setup use Gemini API :

1. Set Up Gemini API Access
2. Setup Environment & Install the SDK
3. Check the available models
4. Write Chatbot Code
5. Modify as per your need
   
## Set Up Gemini API Access : 
* Go to link : **https://makersuite.google.com/app/apikey**
* **Generate an API key**: Click on Create API key, select Project, Generate.
  ![image](https://github.com/user-attachments/assets/aea5b22f-a6f4-4fe2-8e3c-ebe401f1eb10)
* Copy the key and save it somewhere, as it will be used while calling API.

## Setup Environment & Install the SDK :
Setup Virtual Environment First :

```python
python3 -m venv venv
source /bin/activate
```

## install Google generative ai package : 

```python
pip install google-generativeai
```
 
## Check the available models
Let's first check the existing models, than we gonna select the model to be used, run the below given code for getting the available gemini models:

```python
import google.generativeai as genai
import os
```

## Access the API key from the environment variable (or your hardcoded version)
```python
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    API_KEY = "YOUR_ACTUAL_API_KEY"  # Use your hardcoded key if needed

genai.configure(api_key=API_KEY)

print("Available Gemini models:")
for m in genai.list_models():
    print(f"  Name: {m.name}")
    print(f"  Supported methods: {m.supported_generation_methods}")
    print("-" * 20)

Output will be Like : 
"""
Available Gemini models:
  Name: models/chat-bison-001
  Supported methods: ['generateMessage', 'countMessageTokens']
--------------------
  Name: models/text-bison-001
  Supported methods: ['generateText', 'countTextTokens', 'createTunedTextModel']
--------------------
  Name: models/embedding-gecko-001
  Supported methods: ['embedText', 'countTextTokens']
--------------------
  Name: models/gemini-1.0-pro-vision-latest
  Supported methods: ['generateContent', 'countTokens']
--------------------
  Name: models/gemini-pro-vision
  Supported methods: ['generateContent', 'countTokens']
--------------------
.
.
.
etc etc
"""
```
 
## Write Chatbot Code : 
Use below code to get your code run : 

```python
import google.generativeai as genai
import os
```

## Access the API key
```python
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    API_KEY = "Your API Key buddy"
```

## Configure the API key
```python
genai.configure(api_key=API_KEY)
```

## Load the Gemini 1.5 Flash model
```python
model = genai.GenerativeModel("models/gemini-1.5-flash-latest")

def chat_with_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

# Simple chatbot loop
if __name__ == "__main__":
    print("Gemini Chatbot - type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = chat_with_gemini(user_input)
        print("Gemini:", reply)

Output : 
"""
Gemini Chatbot - type 'exit' to quit
You: Hi chatbot how are you 
Gemini: I'm doing well, thank you for asking!  How are you today?

"""
```

<h3 align="center">**Thank you for reading this**</h3>
                                                                                 

​
