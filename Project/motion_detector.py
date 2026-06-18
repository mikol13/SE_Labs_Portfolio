import cv2
import numpy as np

class MotionDetector:
    def __init__(self, threshold=25, min_contour_area=500):
        self.threshold = threshold
        self.min_contour_area = min_contour_area
        self.prev_frame = None
        self.motion_state = False

    def process_frame(self, frame):
        if frame is None:
            return False

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if self.prev_frame is None:
            self.prev_frame = gray
            return False

        frame_delta = cv2.absdiff(self.prev_frame, gray)
        thresh = cv2.threshold(frame_delta, self.threshold, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        contours, _ = cv2.findContours(
            thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
        )

        for contour in contours:
            if cv2.contourArea(contour) >= self.min_contour_area:
                self.motion_state = True
                break

        self.prev_frame = gray
        return self.motion_state
