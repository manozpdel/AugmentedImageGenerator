## Image Gaussian Blur Script

This Python script facilitates the application of Gaussian blur to images using the OpenCV library.

### Description

The script provides a function `apply_blur(image, kernel_size)` to apply Gaussian blur to images. It traverses through a directory containing images in PNG or JPG format, applies the specified kernel size to each image, and saves the blurred images in an output directory.

### Usage

1. Place the images requiring Gaussian blur into the designated input directory (`cats/` in this script).
2. Execute the script. It generates a directory named `blurred_images` within the input directory (if it doesn't exist), and it stores the blurred images there.
3. You can adjust the blur intensity by modifying the `kernel_size` variable in the script. The default kernel size is set to 3.

### Requirements

- Python 3.x
- OpenCV library (cv2)
- NumPy library (numpy)

### Example

```python
# Define the size of the Gaussian kernel for blur
kernel_size = 3  # Adjust as needed
```

### Note

- Ensure the input directory contains images in PNG or JPG format.
- The script overwrites existing files with the same name in the output directory.

