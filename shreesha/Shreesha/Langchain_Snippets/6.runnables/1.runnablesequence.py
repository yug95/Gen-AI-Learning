from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)


llm = HuggingFaceEndpoint(
   repo_id="Qwen/Qwen3-Coder-480B-A35B-Instruct",  
   task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()


# Second prompt that explains a joke
prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',# Template for explaining the joke
    input_variables=['text']
)

# Chain to generate a joke: prompt -> model -> string parser
joke_gen_chain = RunnableSequence(prompt1, model, parser)

# Parallel chain to handle two things:
# 1. Just pass the joke text as-is to next step
# 2. Also send the same joke to another chain that explains it
parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),                              # Directly pass the joke without modifying
    'explanation': RunnableSequence(prompt2, model, parser)     # Run explanation prompt -> model -> parser
})

# Final full chain:
# Step 1: Generate the joke
# Step 2: Use the joke as input to both 'joke' and 'explanation' branches in parallel
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

print(chain.invoke({'topic':'AI'}))