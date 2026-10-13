from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model="llama3.2")

prompt= PromptTemplate(
    template='Write a summary of the following poem - \n {poem}',
    input_variable= ['poem']
)

parser=StrOutputParser()

loader= TextLoader('cricket.txt',encoding='utf-8')

docs=loader.load()

chain= prompt | model | parser

result=chain.invoke({'poem': docs[0].page_content})

print(result)