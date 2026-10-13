from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

model = ChatOllama(model="llama3.2")

prompt= PromptTemplate(
    template='Answer the following questions \n {question} from the following text- \n {text}',
    input_variable= ['question','text']
)

parser=StrOutputParser()

url='https://www.flipkart.com/cason-kz-edx-pro-x-iem-wired-earphones-in-ear-monitor-headphones-gaming/p/itm31cd12526189a?pid=ACCHCKZXMW8AYPGN&lid=LSTACCHCKZXMW8AYPGNXN7NCF&marketplace=FLIPKART&q=iem+earphones&store=0pm%2Ffcn%2F821&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_4_na_na_na&fm=search-autosuggest&iid=393e1ed9-0872-427e-aa43-07ba9a0a9b1d.ACCHCKZXMW8AYPGN.SEARCH&ppt=sp&ppn=sp&ssid=gu8vm4cbzk0000001791922094421&qH=2d28ac019d114029&ov_redirect=true&ov_redirect=true'
loader=WebBaseLoader(url)

docs=loader.load()

chain= prompt | model | parser
print(chain.invoke({'question':'How is the sound quality of this particular product?','text':docs[0].page_content}))