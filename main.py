import os
from time import strftime
import groq
from groq import Groq

from config import apikey

import speech_recognition as sr
import webbrowser
import openai
import datetime
import random

chatStr=""
def chat(query):
    global chatStr
    # print(chatStr)
    client = Groq(api_key=apikey)  # Add your API key
    chatStr+=f"Vivek: {query}\n Jarvis: "


    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content":chatStr
            }
        ],
        temperature=1,
        max_tokens=1024,  # Corrected parameter
        top_p=1
    )

    response_text = ""  # Initialize an empty string to store the response

    for choice in completion.choices:
        if choice.message and choice.message.content:
            response_text += choice.message.content
            # print(choice.message.content, end="")  # Print in real-time
    speaker.Speak(response_text)
    chatStr+=f"{response_text}\n"
    return response_text



    with open(f"Openai/prompt-{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
        f.write(text)







def ai(prompt):
    client = Groq(api_key=apikey)  # Add your API key
    text = f"Groq response for Prompt: {prompt} \n *********************\n\n"

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt  # Corrected here
            }
        ],
        temperature=1,
        max_tokens=1024,  # Corrected parameter
        top_p=1
    )

    response_text = ""  # Initialize an empty string to store the response

    for choice in completion.choices:
        if choice.message and choice.message.content:
            response_text += choice.message.content
            # print(choice.message.content, end="")  # Print in real-time

    text += response_text

    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/prompt-{''.join(prompt.split('intelligence')[1:])}.txt", "w") as f:
        f.write(text)





import win32com.client  #Uses the win32com.client library to directly access the Windows Speech API (SAPI).
from speech_recognition import Recognizer, Microphone
from wikipedia import languages

speaker = win32com.client.Dispatch(
    "SAPI.SpVoice")  #hello i am jarvis your virtual assistant initializes a text-to-speech (TTS) engine using the Windows Speech API (SAPI)

speaker.Rate = 1
# s=input()
# speaker.Speak(s)
speaker.Speak("hello I am Jarvis A I your virtual assistant , how can I help you?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said:{query}")
            return query
        except Exception as e:
            return "Some Error Occured. Sorry ,Try Again"


while True:
    print("listening...")
    query = takeCommand()
    sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"],
             ["instagram", "https://instagram.com"], ["facebook", "https://facebook.com"],
             ["chat gpt", "https://chatgpt.com"], ["google", "https://google.com"],
             ["gmail", "https://mail.google.com/mail/u/1/#inbox"],
             ["college id", "https://mail.google.com/mail/u/2/#inbox"],["student portal","https://student.tnpnsut.in/#/"]]
    if "kill the program" in query:
        query = "killing the program"
        speaker.Speak(query)
        break
    # speaker.Speak(query)
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            speaker.Speak(f"opening {site[0]} sir...")
            webbrowser.open(site[1])
    if "play my playlist".lower() in query.lower():
        speaker.Speak("here's your playlist sir, play according to your mood")
        webbrowser.open("https://open.spotify.com/playlist/4O565stLq6qnBysPXrSXk1?si=71f09f99543145fc")
    # if "play Loose Yourself" in query:
    #     musicPath = "D:\vivek\DesktopAssistantAI\videoplayback.weba"
    #     os.system(f"open {musicPath}")

    elif "the time".lower() in query.lower():
        strfTime = datetime.datetime.now().strftime("%H:%M:%S")
        speaker.Speak(f"sir the time is {strfTime}")

    # if "open vs code".lower() in query.lower():
    #     os.system(f"open C:\Users\DELL\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code")


    #openai
    elif "using artificial intelligence".lower() in query.lower():
        ai(prompt=query)
        speaker.Speak("done sir")


    else:
        chat(query)
