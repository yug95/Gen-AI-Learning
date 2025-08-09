from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Define the model
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()


template = PromptTemplate(
    # The main prompt text with placeholders.
    # {topic} → will be filled in when we run the chain.
    # {format_instruction} → will be filled in right now with JSON formatting rules.
    template='Give me name,age and city of {topic} \n {format_instruction}',

    # This tells PromptTemplate that we’ll give it the value for "topic" later.
    input_variables=['topic'],

    # This fills {format_instruction} immediately with instructions from the parser
    # telling the AI exactly how to output the result in valid JSON.
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'fictional character'})

print(result)
