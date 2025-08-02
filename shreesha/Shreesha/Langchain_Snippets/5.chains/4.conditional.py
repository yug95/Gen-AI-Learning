from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

llm = HuggingFaceEndpoint(
   repo_id="mistralai/Mistral-7B-Instruct-v0.3",  
   task="text-generation"
)

# define model
model = ChatHuggingFace(llm=llm)

# Output parser to return plain text
parser = StrOutputParser()

# Define structured output schema for sentiment classification
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

# Structured parser using the Feedback schema
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# Prompt to classify feedback sentiment
prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

# Create a classification chain: prompt → model → structured parser
classifier_chain = prompt1 | model | parser2

# Prompt to generate response to positive feedback
prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

# Prompt to generate response to negative feedback
prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

# Branch chain to choose response path based on sentiment
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),   # If positive, use positive prompt
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),   # If negative, use negative prompt
    RunnableLambda(lambda x: "could not find sentiment")               # Fallback if no match
)

# Final pipeline: classify first, then respond based on classification
chain = classifier_chain | branch_chain

# Test the chain with a sample feedback
print(chain.invoke({'feedback': 'This is a beautiful phone'}))