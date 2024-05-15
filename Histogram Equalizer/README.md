# Image Histogram Equalization Script

## Description

This Python script performs histogram equalization on images using the OpenCV library. Histogram equalization is a technique used to enhance the contrast of images, making features more distinguishable. The script traverses through a directory containing images in PNG or JPG format, applies histogram equalization to each image, and saves the processed images in an output directory.

## Usage

1. **Place Images in Input Directory**: Place the images you want to enhance into the designated input directory (e.g., `cats/` in this script).
2. **Execute the Script**: Run the script. It will create a directory named `equalized_images` within the input directory (if it doesn't already exist) and store the equalized images there.
3. **View Results**: The script processes each image, applying histogram equalization, and saves the enhanced images with the prefix `equalized_` in the output directory.

## Requirements

- Python 3.x
- OpenCV library (`cv2`)

Install OpenCV using pip if not already installed:
```bash
pip install opencv-python
```

## Example

```python
# Convert image to grayscale if it's in color
if len(image.shape) > 2:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
else:
    gray_image = image
```

## Note

- Ensure the input directory contains images in PNG or JPG format.
- The script creates an output directory within the input directory to store the equalized images.
- The equalized images are saved with the prefix `equalized_` to distinguish them from the original images.
