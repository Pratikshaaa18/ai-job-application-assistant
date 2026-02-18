from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List

import os
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

class JobDetails(BaseModel):
    job_title: str
    required_skills: List[str]
    experience_required: int
    tools: List[str]
    soft_skills: List[str]

parser = PydanticOutputParser(pydantic_object=JobDetails)

prompt = PromptTemplate(
    template="""
You are an expert job description analyzer.

Extract structured job information.

Rules:
- experience_required must be an integer (years)
- Use empty list if information is missing

{format_instructions}

Job Description:
{job_description}
""",
    input_variables=["job_description"],
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

def analyze_job(job_description: str) -> JobDetails:
    return chain.invoke({"job_description": job_description})
