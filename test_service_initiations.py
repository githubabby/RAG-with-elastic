# import modules
from dotenv import load_dotenv
load_dotenv()

from manage_blob import list_containers 
# check if the services are working as expected.

# storage blob accessible
# container present
def test_sample_container_present():
    assert 'sample-documents' in list_containers()
    
# blobs present in container

# elastic search accesible
# search index present
# documents present in the index
# search working

if __name__=="__main__":
    test_sample_container_present()