from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
LLM=HuggingFacePipeline.from_model_id(
    model_id='Qwen/Qwen3-0.6B',
    task='text-generation',
    pipeline_kwargs={
        "temperature": 0.5
    }
)
model=ChatHuggingFace(llm=LLM)
result=model.invoke("hello")
print(result.content)