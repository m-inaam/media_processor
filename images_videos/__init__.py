from images_videos import video_processor
from image_processor import ImageProcessor

if __name__ == "__main__":
    main_directory = 'C:/Users/muham/OneDrive/Desktop/computer-vision/Resources'

    video_processor_instance = video_processor.VideoProcessor(main_directory)
    video_processor_instance.process_videos()

    photo_folder_name = 'Photos'
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

    image_processor = ImageProcessor(main_directory, photo_folder_name, image_extensions)
    image_processor.process_images()
