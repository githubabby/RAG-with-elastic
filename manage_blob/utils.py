# import modules
import os

# create path_exists_isfile
def path_exists_isfile(Path):
    '''Check if the path exists and is a file.'''
    if os.path.exists(Path):
        if os.path.isfile(Path):
            return True
    return False

