import unittest
from unittest.mock import patch, Mock
import cv2 as cv
from structure.video_processor import VideoProcessor


class TestVideoProcessor(unittest.TestCase):

    @patch('cv2.VideoCapture')
    def test_video_processor_initialization(self, mock_VideoCapture):
        mock_cam = Mock()
        mock_VideoCapture.return_value = mock_cam
        mock_cam.isOpened.return_value = True

        vp = VideoProcessor()
        self.assertTrue(vp.cam.isOpened())

    @patch('cv2.VideoCapture')
    def test_video_processor_frame_read(self, mock_VideoCapture):
        mock_cam = Mock()
        mock_VideoCapture.return_value = mock_cam
        mock_cam.isOpened.return_value = True
        mock_cam.read.return_value = (True, 'frame')

        vp = VideoProcessor()
        ret, frame = vp.cam.read()
        self.assertTrue(ret)
        self.assertEqual(frame, 'frame')



if __name__ == '__main__':
    unittest.main()
