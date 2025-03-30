import os

import openai
from groq import Groq
from config import apikey

client = Groq(api_key=apikey)  # Add your API key

completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "write an email to boss for resignation"
        }
    ],
    temperature=1,
    max_completion_tokens=1024,
    top_p=1,
    stream=True,
    stop=None,
)

response_text = ""  # Initialize an empty string to store the response

for chunk in completion:
    text_part = chunk.choices[0].delta.content or ""
    response_text += text_part  # Concatenate chunks
    print(text_part, end="")  # Print in real-time

# Now the full response is stored in `response_text`
print(response_text)  # Print the complete response after streaming











