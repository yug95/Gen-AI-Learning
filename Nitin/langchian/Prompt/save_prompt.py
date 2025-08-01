
# this will create a json file of the prompt that can be used using load_prompt from langchain_core.prompts


from langchain_core.prompts import PromptTemplate

templete = PromptTemplate(template="tell me the capital of {state}", input_variables=["state"],)

templete.save("prompt.json")