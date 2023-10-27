import openai
import json
import sys
import tempfile
import os
import threading
import pyttsx3
from nltk import sent_tokenize

# Put your URI endpoint:port here for your local inference server (in LM Studio)
openai.api_base = 'http://localhost:1234/v1'
# Put in an empty API Key
openai.api_key = ''

# Read context from the text file
with open('context.txt', 'r') as file:
    context = file.read()

# Adjust the following based on the model type
# Alpaca style prompt format:
prefix = "### Instruct:\n"
suffix = "\n### Response:"

# 'Llama2 Chat' prompt format:
# prefix = "[INST]"
# suffix = "[/INST]"

# Initialize sentences as an empty string
sentences = ""

# This is a simple wrapper function to allow you to simplify your prompts
def get_completion(prompt, model="local model", temperature=0.3):
    global sentences  # Declare sentences as a global variable
    formatted_prompt = f"{prefix}{prompt}{suffix}"
    messages = [{"role": "system", "content": context}, {"role": "user", "content": formatted_prompt}]

    # Use OpenAI's ChatCompletion to get a streaming response
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        stop="###",
        temperature=temperature,
        max_tokens=1024,  # Adjust this based on your requirements
        stream=True
    )

    # Process the streaming response
    
    for chunk in response:
        try:
            content = json.loads(str(chunk))
            content_string = content['choices'][0]['delta']['content']
            sys.stdout.write(content_string)
            sys.stdout.flush()

            # Append to sentences
            sentences += content_string

            # Check for sentence completion
            if sentences.endswith(".") or sentences.endswith("?") or sentences.endswith("!") or sentences.endswith(",") or sentences.endswith(";") or sentences.endswith(":") or sentences.endswith("--") or sentences.endswith("...") or sentences.endswith(")") or sentences.endswith("}") or sentences.endswith("]"):
                start_tts_thread(sentences)
                sentences = ""  # Reset sentences
        except (KeyError, json.JSONDecodeError):
            pass

# Create a lock to ensure only one TTS thread runs at a time
tts_lock = threading.Lock()

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def start_tts_thread(text):
    with tts_lock:
        tts_thread = threading.Thread(target=text_to_speech, args=(text,))
        tts_thread.start()
        tts_thread.join()  # Wait for the TTS thread to finish before starting a new one

while True:
    user_input = input("\n\nInput: ")
    if user_input.lower() == 'exit':
        break
    get_completion(user_input, temperature=0.3)
