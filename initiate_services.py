# import modules
from manage_blob import get_or_create_container, upload_or_modify_blob
from utils.utils import list_files

# define constants
container_name = "sample-documents"
upload_documents_path = "sample-documents"

# initialise services
container_client = get_or_create_container(container_name)
files_path_list = list_files(upload_documents_path)
for file_path in files_path_list:
    upload_or_modify_blob(container_name, file_path)