import os
import openai

openai.api_key = "your api key"

response = openai.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [ 
        {
            "role":"user" , "content": "Hi Chatgpt ,say hi back"
        }
    ]

)

answer = response.choices[0].message.content
