## Image Scaling Utility

This Python script provides a utility to scale images by specified factors for width and height. It utilizes the OpenCV library for image processing.

### Features:
- **Image Scaling Functionality**: The `scale_image` function resizes an input image based on specified scaling factors for width and height.
- **Batch Processing**: The script can process multiple images located in a specified directory and save the scaled images in a separate output directory.
- **Customizable Scaling Factors**: Users can adjust the scaling factors for width and height according to their requirements.

### Usage:
1. **Set Input Directory**: Define the path to the directory containing the input images.
2. **Set Output Directory**: Specify the directory where the scaled images will be saved. If it doesn't exist, the script will create it.
3. **Adjust Scaling Factors**: Customize the scaling factors for width and height (`scale_width` and `scale_height` variables).
4. **Run the Script**: Execute the script to process the images and generate scaled versions in the output directory.

### Example:
```python
python scale_images.py
```

### Requirements:
- Python 3.x
- OpenCV library (`cv2`)

### Notes:
- The script assumes that the input images are in PNG or JPG format.
- Make sure to install the required dependencies before running the script.

