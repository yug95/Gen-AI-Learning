import streamlit as st
from langchain_community.document_loaders import PyPDFLoader 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
import os
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
import asyncio

# key is changed do not try this 
os.environ["GOOGLE_API_KEY"] = "AIzaSyCt8ErmkHOQ5fg7Q2bp_2LmiUQeHPSOOoI"
model = GoogleGenerativeAI(model = "gemini-1.5-flash",)


# here the pdf is processed to make machine understand the pdf content 
def process_pdf(pdf_file):
    #don't know what exactly this try block did but fixed the event loop error TODO: know what this block did  
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        asyncio.set_event_loop(asyncio.new_event_loop())
    
    #upload file is save with name temp.pdf because PyPDFLoader needs the path of the file. The content of the file is then splited, embedded and stored in FAISS.
    try:
        with open("temp.pdf", "wb") as f:
            f.write(pdf_file.getvalue())
        
        loader = PyPDFLoader("temp.pdf")
        pages = loader.load_and_split()

        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(pages)

        
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        
        vectorstore = FAISS.from_documents(docs, embeddings)
        
        os.remove("temp.pdf")
        
        return vectorstore
    except Exception as e:
        st.error(f"Error processing PDF: {e}")
        return None


def main():
    st.title("pdf expext")
    pdf_file = st.file_uploader(label="upload file here", type="pdf")
    if pdf_file:
        
        st.success("File uploaded")
        
        vectorstore =  process_pdf(pdf_file)
        if vectorstore:
            # in system {context} is the uploaded document and {input} is the user input i.e question 
            # qa_chain connect the llm and the user input 
            # chain connect the qa_chain(LLM + input) and retriever. 
            # vectorstore.as_retriever() --helps to find the relevant chunks from the context on the bases of the user input 
            system_prompt = (
                            "Use the given context to answer the question. "
                            "If you don't know the answer, say you don't know. "
                            "Use three sentence maximum and keep the answer concise. "
                            "Context: {context}"
                            )
            prompt = ChatPromptTemplate.from_messages([
                            ("system", system_prompt),
                            ("human", "{input}"),
                        ])
            
            
            qa_chain = create_stuff_documents_chain(model, prompt)

            chain = create_retrieval_chain(vectorstore.as_retriever(), qa_chain)
            
            question = st.text_input(label="ask you question")

            #display the response 
            if question:
                with st.spinner("processing..."):
                    try:
                        response = chain.invoke({"input": question})
                        st.write(response["answer"] )

                    except Exception as e:
                        st.error(f"An error occurred: {e}")
        else: 
            st.error("Error processing the pdf")

main()  
