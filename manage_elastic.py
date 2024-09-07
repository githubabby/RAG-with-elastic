# import modules
import os
import requests

from langchain_elasticsearch import ElasticsearchStore

# create_index function
def create_index(IndexName=os.getenv('INDEX_NAME')):
    requests.put(
        url=f"{os.getenv('ES_URL')}/{IndexName}"
    )

# get_elastic_vectorstore function
def get_elastic_vectorstore(Embeddings):
    return ElasticsearchStore(
            es_url=os.getenv('ES_URL'),
            index_name=os.getenv('INDEX_NAME'),
            embedding=Embeddings,
            es_user=os.getenv('ELASTIC_USER'),
            es_password=os.getenv('ELASTIC_PASSWORD'),
        )

# get_document_by_similarity_search function
def get_similar_documents(Query, VectorStore, k=1):
    return VectorStore.similarity_search_with_score(Query, k)
