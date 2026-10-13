from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader= DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs=loader.load()  #use load func when we have small amount of document it loads all document at one time
docs=loader.lazy_load()  #use lazy_load func when we have large amount of document it loads one document at one time 



print(len(docs[0].page_content))

print(docs[0].metadata)
