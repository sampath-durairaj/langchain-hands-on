import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_core.tools import Tool
from langchain_classic.chains import LLMChain
#from langchain.agents import Tool
import logging

from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")
API_KEY = os.getenv("API_KEY")
print(f"Loaded API Key: {API_KEY}")
# Additional code for Lanchain_LLN_Prompt_Template.py can be added here
# For example, you might want to define a function that uses the API key
def use_api_key():
    if API_KEY:
        print("Using the API key for some operation...")
        # Placeholder for actual API usage
    else:
        print("API key is not set.")
use_api_key()

try:
    query = "What is langGraph in LangChain?"
    summary_text = """ LangGraph is a component of LangChain that provides a graph-based representation of language models and their interactions. It allows users to visualize and manage the relationships between different language model components, making it easier to build complex applications that leverage multiple models and tools.
    LangGraph helps in organizing and structuring the way language models are used within LangChain,"""
   
    print(query)
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=API_KEY)

    #Tool 1
    qa_prompt = PromptTemplate.from_template("Answer the following question: {question}")
    qa_chain = LLMChain(llm=llm, prompt=qa_prompt)
    #Wrap the chain in a Tool
    qa_tool = Tool(description = " A basic LLM Chain that answers clear answers" ,
                    name="Sample QA", func=qa_chain.run)

    #Tool 2
    summary_prompt = PromptTemplate.from_template("Answer the following question: {test}")
    summary_chain = LLMChain(llm=llm, prompt=summary_prompt)
    #Wrap the chain in a Tool
    summary_tool = Tool(description = "Summarizes the answer" ,
                    name="Summarizer", func=summary_chain.run)

    qa_response = qa_tool.run(query)
    summary_response = summary_tool.run(summary_text)
except Exception as e:
    print(f"An error occurred: {e}")
    response = None

print("qa_response : " ,qa_response)
print("summary_response : " ,summary_response)






