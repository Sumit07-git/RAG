from langchain_text_splitters import RecursiveCharacterTextSplitter

text="""Artificial Intelligence is transforming the way we live, work, and communicate. It helps computers learn from data, recognize patterns, and make intelligent decisions. Machine learning is an important part of AI that allows systems to improve their performance through experience. Large Language Models can understand and generate human-like text. These models are used in chatbots, virtual assistants, and content generation tools. However, running large AI models requires significant memory and computational power. Techniques such as quantization help reduce memory usage and improve efficiency. As AI continues to evolve, it will play an increasingly important role in our daily lives."""

splitter=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
)

chunks=splitter.split_text(text)
print(len(chunks))
print(chunks)
