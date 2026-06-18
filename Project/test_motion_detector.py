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
        
    # Test 2
	def test_motion_detected_on_visual_change(self):
		frame1 = np.zeros((480, 640, 3), dtype=np.uint8)
		frame2 = np.zeros((480, 640, 3), dtype=np.uint8)
		cv2.rectangle(frame2, (200, 200), (400, 400), (255, 255, 255), -1)

		self.detector.process_frame(frame1)
		result = self.detector.process_frame(frame2)

		self.assertTrue(result, "Failed to detect motion when a large object appeared!")


 if __name__ == "__main__":
    unittest.main(verbosity=2)
