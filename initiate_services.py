# load env variables
import os
from dotenv import load_dotenv
load_dotenv()

# import modules
from manage_blob import (
    get_or_create_container, 
    upload_or_modify_blob, 
    create_documents_from_container
    )
from manage_elastic import (
    create_index, 
    get_elastic_vectorstore, 
    get_similar_documents
    )
from manage_embedding import get_embeddings_function
from utils.utils import list_files

print("service initiation")
# define constants
container_name = "sample-documents"
upload_documents_path = "sample-documents"
query = "what are features of langchain?"

# set base dir
os.environ['BASE_DIR_PATH'] = os.path.dirname(os.path.realpath(__file__))

# initialise services
container_client = get_or_create_container(container_name)
files_path_list = list_files(upload_documents_path)
for file_path in files_path_list:
    upload_or_modify_blob(container_name, file_path)

es_vectorstore = get_elastic_vectorstore(Embeddings=get_embeddings_function())
documents = create_documents_from_container(container_name)
create_index()
es_vectorstore.add_documents(documents=documents)
result = get_similar_documents(Query=query, VectorStore=es_vectorstore)
print(result)
print("service initiation complete!!")