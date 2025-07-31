from langchain_core.prompts import PromptTemplate #this imports the PromptTemplate class from the langchain_core package.

# creating an instance of PromptTemplate and assigning it to the variable template
template = PromptTemplate(
    template="""                                    #multi-line string template,It uses placeholders 
Please summarize the research paper titled "{paper_input}" with the following specifications:
Explanation Style: {style_input}  
Explanation Length: {length_input}  
1. Mathematical Details:   #instruct the AI to include math details in the summary when possible and explain them in simple code if relevant.
   - Include relevant mathematical equations if present in the paper.  
   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  
2. Analogies:              #ask the AI to use analogies—like real-world comparisons—to explain difficult concepts more clearly.
   - Use relatable analogies to simplify complex ideas.  
If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.  
Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",
input_variables=['paper_input', 'style_input','length_input'],    # define the names of variables ({paper_input}, {style_input}, {length_input}) that will be injected into the template when used.
#validate_template tells LangChain to verify that all the required variables in input_variables 
# are actually present in the template.
#It avoids runtime errors due to missing variables.
validate_template=True     
)

template.save('template.json')  #This saves the prompt template to a JSON file called template.json 



#simple syntax 

# from langchain_core.prompts import PromptTemplate

# template = PromptTemplate(
#     template="""Your prompt here with {placeholders}""",
#     input_variables=["placeholder1", "placeholder2"],
#     validate_template=True
# )

# template.save("template.json")




