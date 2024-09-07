# import modules
import os

from manage_blob import get_blob_data_from_container
from langchain_core.documents import Document

# create path_exists_isfile
def path_exists_isfile(Path):
    '''Check if the path exists and is a file.'''
    if os.path.exists(Path):
        if os.path.isfile(Path):
            return True
    return False

# create path_exists_isdir
def path_exists_isdir(Path):
    '''Check if the path exists and is a dir.'''
    if os.path.exists(Path):
        if os.path.isdir(Path):
            return True
    return False
    
# create function to load all the files in directory
def list_files(Path):
    file_path_list = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    newpath = os.path.join(dir_path, Path)
    path_exists_isdir(newpath)
    file_path_list = [os.path.join(newpath,filepath) for filepath in os.listdir(newpath) if path_exists_isfile(os.path.join(newpath,filepath))]
    return file_path_list

def create_documents_from_container(ContainerName):
    blob_data = get_blob_data_from_container(ContainerName)
    return [Document(page_content=blob_data[data]) for data in blob_data]