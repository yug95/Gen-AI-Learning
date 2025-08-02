from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

#Step 1: Define the LLMs (models)
llm1 = HuggingFaceEndpoint(
   repo_id="Qwen/Qwen3-Coder-480B-A35B-Instruct",  #or use ChatOpenAI()
   task="text-generation"
)

model1 = ChatHuggingFace(llm=llm1)

llm2 = HuggingFaceEndpoint(
   repo_id="mistralai/Mistral-7B-Instruct-v0.3",  #or use claude.
   task="text-generation"
)

model2 = ChatHuggingFace(llm=llm2)
# Step 2: Define PromptTemplates
# Prompt to generate notes from the input text
prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)
# Prompt to generate questions (quiz) from the input text
prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)
# Prompt to merge both notes and quiz into a final document
prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

# Step 3: Create Chains
# Run notes and quiz generation in parallel
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

# Merge the results of notes and quiz into a final output
merge_chain = prompt3 | model1 | parser
# Full pipeline: parallel → merge
chain = parallel_chain | merge_chain
# Step 4: Input Text
text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.
The advantages of support vector machines are:
Effective in high dimensional spaces.
Still effective in cases where number of dimensions is greater than the number of samples.
Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.
Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.
The disadvantages of support vector machines include:
If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.
SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).
The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""
#step 5: Invoke the chain with input
result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()
