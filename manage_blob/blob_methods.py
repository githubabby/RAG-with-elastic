# import modules
import os

from azure.core.exceptions import ResourceExistsError
from azure.storage.blob import BlobServiceClient
from langchain_core.documents import Document

# might change the path of utils later
from utils.utils import path_exists_isfile

# create get_blob_service_client function
def create_blob_service_client():
    '''Return blob service client.'''
    return BlobServiceClient.from_connection_string(os.getenv('STORAGE_CONN_STRING'))    
    
# create get_or_create_container function
def get_or_create_container(ContainerName):
    '''Return container client by creating container or getting existing one.'''
    bs_client = create_blob_service_client()
    try:
        bs_client.create_container(ContainerName)
    except ResourceExistsError:
        ...
    return bs_client.get_container_client(ContainerName)

# create upload_or_modify_blob function
def upload_or_modify_blob(ContainerName, BlobPath, BlobName=None):
    '''Upload or Modify blob to a container'''
    container_client = get_or_create_container(ContainerName)
    if path_exists_isfile(BlobPath):
        with open(BlobPath, 'rb') as file:
            if not BlobName:
                BlobName = file.name.split('\\')[-1]
            try:
                container_client.upload_blob(BlobName, file)
                print(f"{BlobName} uploaded succesfully!")
            except ResourceExistsError:
                print(f"{BlobName} already exist!")
    # if data is not present log information
    else:
        ...

# function to list containers
def list_containers():
    bs_client = create_blob_service_client()
    return [container.name for container in bs_client.list_containers()]

# create list_blob_in_container function
def list_blob_in_container(ContainerName):
    container_client = get_or_create_container(ContainerName)
    return [name for name in container_client.list_blob_names()]

def get_blob_data_from_container(ContainerName):
    contianer_client = get_or_create_container(ContainerName)
    return {name:contianer_client.download_blob(name).readall() for name in contianer_client.list_blob_names()}

def create_documents_from_container(ContainerName):
    blob_data = get_blob_data_from_container(ContainerName)
    return [Document(page_content=blob_data[data]) for data in blob_data]