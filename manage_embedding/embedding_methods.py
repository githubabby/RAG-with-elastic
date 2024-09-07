# import modules
from langchain_core.embeddings import FakeEmbeddings

# get_embeddings_function
def get_embeddings_function():
    return FakeEmbeddings(size=512)
