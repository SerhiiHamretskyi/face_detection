import pytest
import os
from unittest.mock import patch
from structure.helpers import get_user_input
from structure.helpers import ensure_directory_exists
from structure.helpers import check_if_folder_empty
from structure.helpers import start_camera_if_folder_empty
from structure.helpers import get_path_to_cur_dir
#get_path_to_cur_dir , find_face_encodings  ,load_reference_face are not tested
test_path = "C:\\Users\\andro\\PycharmProjects\\face_detection\\structure\\photos"
def test_get_user_input():
    with patch("builtins.input" , return_value=test_path):
        result = get_user_input()
        assert result == test_path

def test_ensure_directory_exists_positive(tmp_path):
    # Create a temporary directory to simulate an existing directory
    existing_dir = tmp_path / "existing_directory"
    existing_dir.mkdir()  # Create the directory

    # Call the function with the existing directory path
    ensure_directory_exists(existing_dir)

    # Check if the directory still exists
    assert os.path.exists(existing_dir)  # Should be True

def test_ensure_directory_exists_negative(tmp_path):
    # Create a path that does not exist
    new_dir = tmp_path / "new_directory"

    # Call the function with the new directory path
    ensure_directory_exists(new_dir)

    # Check if the new directory was created
    assert os.path.exists(new_dir)  # Should be True

def test_check_if_folder_empty_with_empty_dir(tmp_path):
    # Use tmp_path to create an empty directory
    empty_dir = tmp_path / "empty_directory"
    empty_dir.mkdir()

    # Call the function and verify it detects the directory as empty
    result = check_if_folder_empty(empty_dir)
    assert result is True, "Expected the function to return True for an empty directory."

def test_check_if_folder_empty_with_files(tmp_path):
    # Use tmp_path to create a directory and add a file to it
    non_empty_dir = tmp_path / "non_empty_directory"
    non_empty_dir.mkdir()
    (non_empty_dir / "test_file.txt").write_text("This is a test file.")

    # Call the function and verify it detects the directory as not empty
    result = check_if_folder_empty(non_empty_dir)
    assert result is False, "Expected the function to return False for a non-empty directory."

def test_start_camera_if_folder_empty_with_empty_folder(tmp_path):
    """Test when the folder is empty."""
    # Create an empty temporary directory
    empty_folder = tmp_path / "empty_folder"
    empty_folder.mkdir()  # Create the directory

    # Call the function and verify the result
    result = start_camera_if_folder_empty(str(empty_folder))
    assert result is True, "Expected True when the folder is empty, but got False."

def test_start_camera_if_folder_empty_with_non_empty_folder(tmp_path):
    """Test when the folder contains files."""
    # Create a temporary directory with a file in it
    non_empty_folder = tmp_path / "non_empty_folder"
    non_empty_folder.mkdir()
    (non_empty_folder / "test_file.txt").write_text("Sample content")  # Add a file

    # Call the function and verify the result
    result = start_camera_if_folder_empty(str(non_empty_folder))
    assert result is False, "Expected False when the folder is not empty, but got True."