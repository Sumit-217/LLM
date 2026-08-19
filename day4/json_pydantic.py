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

# structure
from pydantic import BaseModel
class Ticket(BaseModel):
    name: str
    email: str
    issue: str

schema= Ticket.model_json_schema()

response_format = {
    "type": "json_object"
}

system_prompt = f"""
    Extract the personal information from this ticket strictly based on this schema in JSON format.{schema}
"""

message_system = {
    "role": "system",
    "content": system_prompt
}

text = "Hii, My name is Sumit and i buy a iphone and now it is not working at all, my address is delhi. My email is abc@gmail.com. My contact number is 1234567890." \

prompt = f"""
This is a Customer Ticket. You have to extract the following information from the text {text}
"""

message = {"role": role, "content": prompt}

messages = [message_system,message]

response = client.chat.completions.create(model=model, messages=messages, temperature=2 , response_format = response_format)

answer = response.choices[0].message.content
print(answer)

# how to read json
import json
raw_json = answer
data_file = json.loads(raw_json)
ticket = Ticket(**data_file)

# we can pass these to further parsing or another code
print(ticket.name)
print(ticket.email)
print(ticket.issue)


