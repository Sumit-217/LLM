import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from time import sleep

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY kaha hai???")

client = Groq(api_key=my_api_key)
model="openai/gpt-oss-120b"

JD="""
    We are hiring a Backend Python Developer.
        Requirements:
        - Strong Python
        - FastApi or Django experience
        - PostgreSQL or MySQL experience
        - Docker
        - AWS
        - REST APIs
        -2+ years of experience
"""
RESUME = """
    Name: Sumit Kumar
    Experience:
    - Backend Python Developer at XYZ Company (2020-2023)

    Skills:
    - Python
    - FastApi
    - Django
    - PostgreSQL
    - MySQL
    - Docker
    - AWS
    - REST APIs

    Projects:
    - Developed a REST API for an e-commerce platform using FastApi and PostgreSQL.
    Deployed the application on AWS using Docker containers.
"""

# RESUME = """
#     Name: Sumit Kumar
#     Experience:
#     - frontend Developer at XYZ Company (2020-2023)

#     Skills:
#     - Javascript
#     # - FastApi
#     - React
#     - PHP
#     - MYSQL
#     # - Docker
#     - AWS
#     # - REST APIs

#     Projects:
#     - Developed a e-commerce platform using React and MySQL.
# """

def ask_llm(system_prompt, user_prompt):
    sys_msg = {"role": "system", "content": system_prompt}
    user_msg = {"role": "user", "content": user_prompt}

    response = client.chat.completions.create(
        model=model,
        messages=[
            sys_msg,
            user_msg 
        ],
        max_tokens=2000,
        temperature=0.7
    )
    answer =answer = response.choices[0].message.content
    return answer

def  step1_res_extract():
    # extract skills, experience, and projects from the resume
    system_prompt = """You are a professional HR. extracts relevant information from resumes provided. only return the extracted information in a structured format. do not return any other text."""
    user_prompt = f"""Extract the following information from the resume:\n{RESUME}\n\nPlease provide the extracted information in a structured format."""
    extracted_info = ask_llm(system_prompt, user_prompt)
    return extracted_info

def  step2_JD_extract():
    # extract skills, experience, and projects from the job description
    system_prompt = """You are a professional HR. extracts relevant information from job descriptions provided. only return the extracted information in a structured format. do not return any other text."""
    user_prompt = f"""Extract the following information from the job description:\n{JD}\n\nPlease provide the extracted information in a structured format."""
    extracted_info = ask_llm(system_prompt, user_prompt)
    return extracted_info

def step3_match():
    # match the extracted information from the resume and job description
    system_prompt = """You are a professional HR. You have extracted information from a resume and a job description. Your task is to match the candidate's skills, experience, and projects with the requirements of the job description. provide a final score between 1-100 and a short verdict whether the candidate is good fit or not."""
    user_prompt = f"""Resume Information:\n{step1_res_extract()}\n\nJob Description Information:\n{step2_JD_extract()}\n"""
    match_analysis = ask_llm(system_prompt, user_prompt)
    return match_analysis

candidate = step1_res_extract()
sleep(2)
print(candidate)
sleep(2)
job_description = step2_JD_extract()
sleep(2)
print(job_description)
sleep(2)
match_result = step3_match()
sleep(2)
print(match_result)
