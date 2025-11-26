import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
load_dotenv()

google_api_jey = os.getenv("GOOGLE_API_KEY")

google_llm = ChatGoogleGenerativeAI(temperature=0, api_key=google_api_jey, model="gemini-2.5-pro")

#response = google_llm.invoke("Write a poem about AI in the style of Shakespeare.")
#print(response) 


prompt = PromptTemplate(input_variables=["input"], 
                        template="Convert this statement in better english :{input}"
)

chain = prompt | google_llm | StrOutputParser()
response = chain.invoke({"input": "How are you doing"})
print(response)


json_parser = JsonOutputParser(schema={"name": str, "age": int, "city": str})
prompt_json = PromptTemplate(
    input_variables=["input"], 
    template="Extract the name, age, and city from the following text and format it as JSON: {input}"
)
chain_json = prompt_json | google_llm | json_parser
response_json = chain_json.invoke({"input": "John is 30 years old and lives in   New York."})
print(response_json)



