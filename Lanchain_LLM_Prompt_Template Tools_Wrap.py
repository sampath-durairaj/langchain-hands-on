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

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key=API_KEY)

    prompt = PromptTemplate.from_template("Answer the following question: {query}")

   
    print(query)

    #chain = prompt | llm
    chain = LLMChain(llm=llm, prompt=prompt)

    #Wrap the chain in a Tool
    qa_tool = Tool(description = " A basic LLM Chain that answers clear answers" , name="Sample QA", func=chain.run)

    response = qa_tool.run(query)
except Exception as e:
    print(f"An error occurred: {e}")
    response = None

print("Answer : " ,response)

logging.info(response)




