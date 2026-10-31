from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm_groq=ChatGroq(model="openai/gpt-oss-120b")

result=llm_groq.invoke("Hello Llama")
print(result.content)