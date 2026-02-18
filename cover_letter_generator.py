from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


prompt = PromptTemplate(
    template="""
Write a professional cover letter based on the following details.

Job Details:
{job_details}

Candidate Resume:
{resume_text}

Guidelines:
- Professional tone
- 3–4 paragraphs
- Plain text only
- No JSON or bullet points
""",
    input_variables=["job_details", "resume_text"]
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.4,
    google_api_key=GOOGLE_API_KEY
)

parser = StrOutputParser()

chain = prompt | llm | parser

def generate_cover_letter(job_details: str, resume_text: str) -> str:
    return chain.invoke({
        "job_details": job_details,
        "resume_text": resume_text
    })
