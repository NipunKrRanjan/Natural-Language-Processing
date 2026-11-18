from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
LLM=HuggingFaceEndpoint(
    repo_id='LiquidAI/LFM3-1.7B',
    task='text-generation'
)
model=ChatHuggingFace(llm=LLM)
while(True):
    user=input("Enter your query,Type exit to exit the chatbot \n")
    if(user.lower() == 'exit'):
        print("Thank you, have a nice day")
        break
    else:
        result=model.invoke(user)
        print(result.content+'\n')