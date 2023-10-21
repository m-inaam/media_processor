import cv2 as cv
import os

# Main directory path
main_directory = 'C:/Users/muham/OneDrive/Desktop/computer-vision/Resources'

# Photos folder within the main directory
photo_directory = os.path.join(main_directory, 'Photos')

# List all the image files in the photo directory
image_files = [f for f in os.listdir(photo_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

for image_file in image_files:
    # full path of image
    image_path = os.path.join(photo_directory, image_file)

    # Read the image
    img = cv.imread(image_path)

    # Check if the image was loaded successfully before displaying it
    if img is not None:
        # Extract the image file name (without the extension) and use it as the window title
        window_title = os.path.splitext(image_file)[0]
        cv.imshow(window_title, img)
        cv.waitKey(2000)  # Display each image for 2 seconds

cv.destroyAllWindows()  # Close all OpenCV windows when done
