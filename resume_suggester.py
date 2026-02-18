from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List

import os
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

class ResumeSuggestions(BaseModel):
    missing_skills: List[str]
    improvement_points: List[str]
    overall_fit_summary: str

parser = PydanticOutputParser(pydantic_object=ResumeSuggestions)

prompt = PromptTemplate(
    template="""
You are a career coach.

Compare the candidate resume with the job requirements
and suggest improvements.

{format_instructions}

Job Details:
{job_details}

Candidate Resume:
{resume_text}
""",
    input_variables=["job_details", "resume_text"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    google_api_key=GOOGLE_API_KEY
)

chain = prompt | llm | parser

def suggest_resume_improvements(job_details: str, resume_text: str) -> ResumeSuggestions:
    return chain.invoke({
        "job_details": job_details,
        "resume_text": resume_text
    })
