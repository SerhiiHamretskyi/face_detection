import os
from structure.helpers import get_path_to_cur_dir
from structure.helpers import ensure_directory_exists
from structure.helpers import check_if_folder_empty

question_name = input("Provide your name ")
print(question_name)


path_with_name = get_path_to_cur_dir(question_name)
ensure_directory_exists(path_with_name)
check_if_folder_empty(path_with_name)