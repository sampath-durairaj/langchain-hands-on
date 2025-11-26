import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
load_dotenv()

google_api_jey = os.getenv("GOOGLE_API_KEY")

google_llm = ChatGoogleGenerativeAI(temperature=0, api_key=google_api_jey, model="gemini-2.5-pro")

#response = google_llm.invoke("Write a poem about AI in the style of Shakespeare.")
#print(response) 


prompt = PromptTemplate(input_variables=["input"], template="You are a helpful assistant that translates user request :{input}"
)

chain = prompt | google_llm 
response = chain.invoke({"input": "Explain quantum computing in simple terms."})
print(response)