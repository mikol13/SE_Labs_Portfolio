import cv2
from motion_detector import MotionDetector

if __name__ == "__main__":
    video_path = "video.mp4"
    cap = cv2.VideoCapture(video_path)
    detector = MotionDetector(threshold=25, min_contour_area=1000)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        is_moving = detector.process_frame(frame)

        status_text = "MOTION DETECTED" if is_moving else "IDLE"
        color = (0, 0, 255) if is_moving else (0, 255, 0)

        cv2.putText(frame, f"System Status: {status_text}", (10, 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        
        cv2.imshow("Surveillance Prototype Feed", frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
