import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI


from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

google_api_jey = os.getenv("GOOGLE_API_KEY")
oprn_api_key = os.getenv("OPEN_API_KEY")

google_llm = ChatGoogleGenerativeAI(temperature=0, api_key=google_api_jey, model="gemini-2.5-pro")

open_llm = ChatOpenAI(
    model="gpt-3.5-turbo", 
    temperature=0, 
    api_key=oprn_api_key,
    max_completion_tokens=500,
    stop="test",
    timeout=240
    )

#Text Model just one output
open_llm_text_nmodel = OpenAI(
    model="gpt-3.5-turbo-instruct", 
    temperature=0, 
    api_key=oprn_api_key,

    )
#response = google_llm.invoke("Write a poem about AI in the style of Shakespeare.")
#print(response) 


prompt = PromptTemplate(
    input_variables=["input"], 
    template="YWhat is the capital of India :{input}"
)

chat_prompt = ChatPromptTemplate.from_template(
    template="Provide more details"
)

chat_prompt1 = ChatPromptTemplate.from_messages(
    [
        ("system", "Always give correct answer"),
        ("human", "Provide more details :{input}"),
    ]
)
chain = chat_prompt1 | google_llm 
response = chain.invoke({"input": "What is the capital of India?"})

print(response)
