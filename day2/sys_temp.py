import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY kaha hai???")

client = Groq(api_key=my_api_key)
model="openai/gpt-oss-120b"
role = "user"
prompt = "I LOVE YOU!!!"

# System message to set the context for the conversation
msg_sys={"role": "system", "content": "You are my girlfriend"}

message = {"role": role, "content": prompt}

messages = [msg_sys, message]

# bydefault temp is 0 and ranges 0-2
response = client.chat.completions.create(model=model, messages=messages, temperature=2)
# print(response)

print("###############################")
answer = response.choices[0].message.content
print(answer)
