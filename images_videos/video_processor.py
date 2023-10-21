import cv2 as cv
import os

class VideoProcessor:
    def __init__(self, main_directory):
        self.main_directory = main_directory
        self.video_directory = os.path.join(main_directory, 'Videos')

    def process_videos(self):
        video_files = [f for f in os.listdir(self.video_directory) if f.lower().endswith(('.mp4', '.avi', '.mov'))]

        for video_file in video_files:
            video_path = os.path.join(self.video_directory, video_file)

            cap = cv.VideoCapture(video_path)

            if cap.isOpened():
                window_title = os.path.splitext(video_file)[0]
                while True:
                    ret, frame = cap.read()
                    if ret:
                        cv.imshow(window_title, frame)
                        if cv.waitKey(20) & 0xFF == ord('q'):
                            break
                    else:
                        break
                cap.release()
                cv.destroyAllWindows()
            else:
                print(f'Unable to open video file: {video_path}')
