## Image Brightness Adjustment Script

This Python script enables the adjustment of image brightness using the OpenCV library.

### Description:
The script includes a function `adjust_brightness(image, brightness_factor)` to modify the brightness of images. It iterates through a directory containing images in PNG or JPG format, applies the specified brightness factor to each image, and saves the adjusted images in an output directory.

### Usage:
1. Place the images requiring brightness adjustment into the designated input directory (`cats/` in this script).
2. Run the script. It creates a directory named `adjusted_brightness_images` within the input directory (if it doesn't exist), and it stores the adjusted images there.
3. You can adjust the brightness by modifying the `brightness_factor` variable in the script. The default brightness factor is set to 25.

### Requirements:
- Python 3.x
- OpenCV library (`cv2`)
- NumPy library (`numpy`)

### Example:
```python
# Define the brightness factor for adjusting image brightness
brightness_factor = 25  # Increase or decrease as needed
```

### Note:
- Ensure the input directory contains images in PNG or JPG format.
- The script overwrites existing files with the same name in the output directory.
