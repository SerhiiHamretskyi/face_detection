import pytest
import os
from unittest.mock import patch
from structure.helpers import get_user_input
from structure.helpers import ensure_directory_exists
from structure.helpers import get_path_to_cur_dir

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
def test_get_path_to_cur_dir():
    # Use patch to capture the printed output
    with patch('builtins.print') as mock_print:
        cwd = os.getcwd()  # Expected result from os.getcwd()
        result = get_path_to_cur_dir()  # Call the function

        # Check if the print function was called with the expected output
        mock_print.assert_called_once_with(cwd)

        # Verify that the function returns the correct path
        assert result == cwd