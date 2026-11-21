from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding=OpenAIEmbeddings(
    model='text-embedding-3-small',
    dimensions=50
)
result=embedding.embed_query("My name is Nipun")
print(result)