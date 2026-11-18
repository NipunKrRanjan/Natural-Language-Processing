from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm_groq=ChatGroq(model="openai/gpt-oss-120b",temperature=0.5,max_tokens=150)

result=llm_groq.invoke("Make a 5-word line on cars")
print(result.content)
