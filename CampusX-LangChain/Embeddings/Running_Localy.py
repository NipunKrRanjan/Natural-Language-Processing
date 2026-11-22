from langchain_huggingface import HuggingFaceEmbeddings
embedding=HuggingFaceEmbeddings(
    model='sentence-transformers/all-MiniLM-L6-v2',
)
text="My name is Nipun" 
vector=embedding.embed_query(text=text) #For only 1 line of text
print((vector))