import unittest
import numpy as np
import cv2
from motion_detector import MotionDetector

class TestMotionDetector(unittest.TestCase):

    def setUp(self):
        self.detector = MotionDetector(threshold=25, min_contour_area=500)

	# Test 1
    def test_no_motion_for_identical_frames(self):
        frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
        frame2 = np.zeros((480, 640, 3), dtype=np.uint8)

        self.detector.process_frame(frame1)
        result = self.detector.process_frame(frame2)

        self.assertFalse(result, "Falsely detected motion on identical frames!")

 if __name__ == "__main__":
    unittest.main(verbosity=2)
