import shutil
from os import mkdir
from pathlib import Path

# Begin by asking the user to specify a directory path that they want to organize. Use the input()
# function in Python to get this input (see the next video for more details on this).
# Optionally, you can also implement validation logic here, that tests whether the user-supplied
# text string is a valid directory.

# Test urls
#C:\Users\avery\PycharmProjects\PythonProject\PythonProjects4Me\paths_and_folders\project\Requirements.txt



# If you come across a directory with the word "temp" in its name, delete the directory and its contents. Be aware that the requirement is to delete such directories recursively, i.e., any sub-directory with "temp" in i
# ts name should also be deleted regardless of its depth in the directory structure.

def does_exist_then_move(path,path2):
    if path.exists():
        shutil.move(path, path2)
    else:
        print('didnt work')




user_src_folder = input()
user_dir_path = Path(user_src_folder)
folder_creation_list = ["text_files","csv_files","folders"]
if user_dir_path.exists():
    for filename in folder_creation_list:
        closet_creation_path = user_dir_path / 'closet' / filename
        # closet_creation_path.mkdir(exist_ok=True, parents=True)

    for item in user_dir_path.iterdir():
        if item.is_file() and item.suffix == '.txt':
            file_to_move = item.parent / item.name
            file_to_be_placed = user_dir_path / 'closet' / 'csv_files'
            # does_exist_then_move(file_to_move,file_to_be_placed)

        if item.is_file() and item.suffix == '.csv':
            file_to_move = item.parent / item.name
            file_to_be_placed = user_dir_path / 'closet' / 'text_files'
            # does_exist_then_move(file_to_move,file_to_be_placed)

        if item.is_dir() and not item.name == "closet":
            file_to_move = item.parent / item.name
            file_to_be_placed = user_dir_path / 'closet' / 'folders'
            # does_exist_then_move(file_to_move,file_to_be_placed)



    # with open(user_src_folder, 'r') as file:
    #         print(file.read())
else:
    print('file does not exisit')








