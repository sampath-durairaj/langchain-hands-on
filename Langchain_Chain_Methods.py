import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from langchain_core.output_parsers import StrOutputParser

from langchain_core.prompts import ChatPromptTemplate
load_dotenv()

google_api_jey = os.getenv("GOOGLE_API_KEY")
oprn_api_key = os.getenv("OPEN_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

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


prompt = PromptTemplate.from_template(
   "You are a helpful assistant returning output in just plain text. Give me a short bio of the {celebrity} " \
   "in single line "
)

chain = prompt | google_llm | StrOutputParser()



#.Invoke
    #response = chain.invoke({"celebrity": "Rajinikath"})
    #print(response)
#.batch
responses = chain.batch(
    [
        {"celebrity": "Rajinikath"},
        {"celebrity": "Kamalahassan"},
        {"celebrity": "Vijay"},
    ]
)
print(responses)


#.stream
streaming_responses = chain.stream(
    [
        {"celebrity": "Rajinikath"},
        {"celebrity": "Kamalahassan"},
        {"celebrity": "Vijay"},
    ]
)
for resp in streaming_responses:
    for chunk in resp:
        print(chunk)

#.ainvoke
import asyncio
async def main():
    response = await chain.ainvoke({"celebrity": "Rajinikath"})
    print(response)

asyncio.run(main())

#.abatch
async def main_batch():
    responses = await chain.abatch(
        [
            {"celebrity": "Rajinikath"},
            {"celebrity": "Kamalahassan"},
            {"celebrity": "Vijay"},
        ]
    )
    print(responses)    

asyncio.run(main_batch())

#.astream
async def main_stream():
    streaming_responses = await chain.astream(
        [
            {"celebrity": "Rajinikath"},
            {"celebrity": "Kamalahassan"},
            {"celebrity": "Vijay"},
        ]
    )
    async for resp in streaming_responses:
        async for chunk in resp:
            print(chunk)
asyncio.run(main_stream())
