import unittest
from unittest import mock
import cv2 as cv


class TestCameraCapture(unittest.TestCase):

    @mock.patch("cv2.VideoCapture")
    def test_camera_initialization_success(self, MockVideoCapture):
        # Mock the behavior of the camera initialization
        mock_cam = mock.Mock()
        MockVideoCapture.return_value = mock_cam
        mock_cam.isOpened.return_value = True  # Simulate successful camera opening

        # Call the original code to initialize the camera
        cam = cv.VideoCapture(0)

        # Test that the camera was successfully opened
        self.assertTrue(cam.isOpened())

    @mock.patch("cv2.VideoCapture")
    def test_camera_initialization_failure(self, MockVideoCapture):
        # Mock the behavior of the camera initialization failure
        mock_cam = mock.Mock()
        MockVideoCapture.return_value = mock_cam
        mock_cam.isOpened.return_value = False  # Simulate camera opening failure

        # Call the original code to initialize the camera
        cam = cv.VideoCapture(0)

        # Test that the camera was not opened
        self.assertFalse(cam.isOpened())


