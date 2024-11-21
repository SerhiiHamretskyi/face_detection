import os
from unittest.mock import patch
from unittest import mock
from structure.helpers import get_user_input
from structure.helpers import ensure_directory_exists
from structure.helpers import check_if_folder_empty
from structure.helpers import start_camera_if_folder_empty
from structure.video_processor import load_reference_face


# get_path_to_cur_dir , find_face_encodings  ,load_reference_face are not tested
test_path = "C:\\Users\\andro\\PycharmProjects\\face_detection\\structure\\photos"


def test_get_user_input():
    with patch("builtins.input", return_value=test_path):
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
    assert (
        result is True
    ), "Expected the function to return True for an empty directory."


def test_check_if_folder_empty_with_files(tmp_path):
    # Use tmp_path to create a directory and add a file to it
    non_empty_dir = tmp_path / "non_empty_directory"
    non_empty_dir.mkdir()
    (non_empty_dir / "test_file.txt").write_text("This is a test file.")

    # Call the function and verify it detects the directory as not empty
    result = check_if_folder_empty(non_empty_dir)
    assert (
        result is False
    ), "Expected the function to return False for a non-empty directory."


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


def test_no_face_in_reference_photo():
    with mock.patch("os.listdir", return_value=["photo.jpg"]), mock.patch(
        "face_recognition.load_image_file"
    ) as mock_load_image_file, mock.patch(
        "face_recognition.face_encodings", return_value=[]
    ):  # Mock face_recognition to return no face encodings
        mock_load_image_file.return_value = "mock_image"  # Return a mock image object
        result = load_reference_face("test/path")
        assert (
            result is None
        )  # The function should return None if no face is detected in the image


# Test when a face is successfully detected in the reference photo
def test_face_in_reference_photo():
    mock_encoding = "mock_face_encoding"

    with mock.patch("os.listdir", return_value=["photo.jpg"]), mock.patch(
        "face_recognition.load_image_file"
    ) as mock_load_image_file, mock.patch(
        "face_recognition.face_encodings", return_value=[mock_encoding]
    ):  # Mock face_recognition to return a face encoding
        mock_load_image_file.return_value = "mock_image"  # Return a mock image object
        result = load_reference_face("test/path")
        assert (
            result == mock_encoding
        )  # The function should return the face encoding when a face is detected


# Test when there are multiple files in the folder (optional for your use case)
def test_multiple_files_in_folder():
    mock_encoding = "mock_face_encoding"

    with mock.patch(
        "os.listdir", return_value=["photo1.jpg", "photo2.jpg"]
    ), mock.patch(
        "face_recognition.load_image_file"
    ) as mock_load_image_file, mock.patch(
        "face_recognition.face_encodings", return_value=[mock_encoding]
    ):
        mock_load_image_file.return_value = "mock_image"  # Return a mock image object
        result = load_reference_face("test/path")
        assert (
            result == mock_encoding
        )  # It should return the encoding of the first file


def test_no_reference_photo():
    with mock.patch(
        "os.listdir", return_value=[]
    ):  # Mock os.listdir to return an empty list
        result = load_reference_face("test/path")
        assert result is None  # The function should return None when no files are found
