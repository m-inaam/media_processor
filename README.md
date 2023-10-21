# Media Processor Package

The **Media Processor** package is a Python package designed to help you process both image and video files. This package includes two modules: `video_processor` for working with video files and `image_processor` for working with image files.

## Usage

### Installation

You can install this package using `pip`:

```bash
pip install media-processor

```

## Example Usage

```bash
from media_processor import video_processor, image_processor

# Video processing
main_directory = 'path/to/main/directory'
video_processor_instance = video_processor.VideoProcessor(main_directory)
video_processor_instance.process_videos()

# Image processing
photo_folder_name = 'Photos'
image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')
image_processor_instance = image_processor.ImageProcessor(main_directory, photo_folder_name, image_extensions)
image_processor_instance.process_images()
    
```

## Modules

```bash 
video_processor ``` 

: Contains classes and functions for video processing.
    
    ```bash
image_processor ``` 

: Contains classes and functions for image processing.