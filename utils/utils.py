# import modules
import os

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
    dir_path = os.getenv("BASE_DIR_PATH")
    newpath = os.path.join(dir_path, Path)
    path_exists_isdir(newpath)
    file_path_list = [os.path.join(newpath,filepath) for filepath in os.listdir(newpath) if path_exists_isfile(os.path.join(newpath,filepath))]
    return file_path_list
