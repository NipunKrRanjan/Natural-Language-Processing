from langchain_huggingface import HuggingFaceEmbeddings
embedding=HuggingFaceEmbeddings(
    model='sentence-transformers/all-MiniLM-L6-v2',
)
text="My name is Nipun" 
vector=embedding.embed_query(text=text) #For only 1 line of text
print((vector))

#For multiple line of text
document=[
    "Our model is intended to be used as a sentence and short paragraph encoder.",
    "Given an input text, it outputs a vector which captures the semantic information.",
    "The sentence vector may be used for information retrieval, clustering or sentence similarity tasks.",
    "By default, input text longer than 256 word pieces is truncated."
]

vector_doc=embedding.embed_documents(document)
for value in vector_doc:
    print(str(value)+'\n')