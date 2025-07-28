from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

# Save Hugging Face model cache to D: drive instead of default C: drive
os.environ['HF_HOME'] = 'D:/huggingface_cache'

llm = HuggingFacePipeline.from_model_id(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,          # Controls randomness/creativity
        max_new_tokens=100        # Limits the number of generated tokens
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")

print(result.content)
