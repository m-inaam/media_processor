import cv2 as cv
import os

class ImageProcessor:
    def __init__(self, main_directory, photo_folder_name, image_extensions):
        self.main_directory = main_directory
        self.photo_directory = os.path.join(main_directory, photo_folder_name)
        self.image_extensions = image_extensions

    def process_images(self):
        image_files = [f for f in os.listdir(self.photo_directory) if f.lower().endswith(tuple(self.image_extensions))]

        for image_file in image_files:
            # Full path of the image
            image_path = os.path.join(self.photo_directory, image_file)

            # Read the image
            img = cv.imread(image_path)

            # Check if the image was loaded successfully before displaying it
            if img is not None:
                # Extract the image file name (without the extension) and use it as the window title
                window_title = os.path.splitext(image_file)[0]
                cv.imshow(window_title, img)
                cv.waitKey(2000)  # Display each image for 2 seconds

        cv.destroyAllWindows()  # Close all OpenCV windows when done


