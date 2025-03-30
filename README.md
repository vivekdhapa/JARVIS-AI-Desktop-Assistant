# Jarvis AI - Virtual Assistant

Jarvis AI is a voice-activated virtual assistant powered by Groq's Llama-3.3-70b model, speech recognition, and text-to-speech capabilities. This assistant can respond to user queries, open websites, retrieve the current time, and even generate AI-powered responses using Groq's API.

## Features

- **Voice Recognition:** Uses `speech_recognition` to capture user voice input.
- **Text-to-Speech:** Utilizes Windows Speech API (`win32com.client`) to provide voice responses.
- **AI Chatbot:** Integrates with Groq API for AI-generated responses.
- **Web Automation:** Can open frequently used websites like YouTube, Wikipedia, Instagram, and more.
- **Time Retrieval:** Fetches the current time on command.
- **Spotify Playlist:** Opens a predefined Spotify playlist on request.
- **Custom Commands:** Can be expanded to include more functionalities like opening applications or fetching data from the web.

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- Required Python libraries:
  ```sh
  pip install groq speechrecognition pyaudio openai wikipedia pywin32
  ```
- A valid Groq API key (store it in `config.py` as `apikey = "your_api_key"`)

## Usage

1. Run the script:
2. Speak your command when prompted.
3. The assistant will respond accordingly based on the command.

## Commands Supported

- "Open YouTube" → Opens YouTube in the browser.
- "What is the time?" → Tells the current time.
- "Play my playlist" → Opens a predefined Spotify playlist.
- "Using artificial intelligence" → Calls AI to generate a response.
- "Kill the program" → Terminates the assistant.

## Future Enhancements

- Add more integrations (e.g., controlling smart devices, fetching news updates).
- Enhance the AI model’s responses with additional contextual memory.
- Improve speech recognition accuracy with fine-tuned settings.

##

By Vivek Dhapa
