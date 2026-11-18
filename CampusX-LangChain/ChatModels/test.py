from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm_groq=ChatGroq(model="openai/gpt-oss-120b",temperature=1.8)

while(True):
    user=input("Enter your query,Type exit to exit the chatbot \n")
    if(user.lower() == 'exit'):
        print("Thank you, have a nice day")
        break
    else:
        result=llm_groq.invoke(user)
        print(result.content)