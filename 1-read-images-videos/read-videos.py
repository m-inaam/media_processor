import cv2 as cv
import os  

# Main directory path
main_directory = 'C:/Users/muham/OneDrive/Desktop/computer-vision/Resources'

# Videos folder within the main directory
video_directory = main_directory + '/Videos'

# List all the video files in the video directory
video_files = [f for f in os.listdir(video_directory) if f.lower().endswith(('.mp4', '.avi', '.mov'))]

for video_file in video_files:
    # full path of video
    video_path = os.path.join(video_directory, video_file)

    # Read the video
    cap = cv.VideoCapture(video_path)

    # Check if the video was loaded successfully before displaying it
    if cap.isOpened():
        # Extract the video file name (without the extension) and use it as the window title
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
        cv.destroyAllWindows()  # Close all OpenCV windows when done
    else:
        print(f'Unable to open video file: {video_path}')
        