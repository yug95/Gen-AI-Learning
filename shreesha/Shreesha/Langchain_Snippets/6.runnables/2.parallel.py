from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)


llm = HuggingFaceEndpoint(
   repo_id="Qwen/Qwen3-Coder-480B-A35B-Instruct",  
   task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

# Create a parallel chain to run two different tasks at the same time:
# One generates a tweet, the other a LinkedIn post
parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser),      # Task 1: Generate tweet
    'linkedin': RunnableSequence(prompt2, model, parser)    # Task 2: Generate LinkedIn post
})

result = parallel_chain.invoke({'topic':'AI'})

print(result['tweet'])
print(result['linkedin'])
