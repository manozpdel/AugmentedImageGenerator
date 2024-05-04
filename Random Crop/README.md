**Random Image Cropper**

**Description**:
This repository contains a Python script for randomly cropping images using OpenCV library. The script `random_image_cropper.py` utilizes functions from OpenCV (`cv2`) and NumPy (`np`) to load images from a specified directory, randomly crop them to a predefined size, and save the cropped images in a separate directory.

**Features**:
- Randomly crops images to a specified size.
- Supports both PNG and JPG image formats.
- Provides flexibility to adjust crop dimensions.

**Usage**:
1. Clone the repository to your local machine.
2. Install the required dependencies (OpenCV and NumPy).
3. Place your images in the specified directory (`cats/` in the provided script).
4. Run the script `random_image_cropper.py`.
5. Cropped images will be saved in the `cropped_images` directory within the input directory.

**Example**:
```python

# Define crop dimensions
crop_height = 50
crop_width = 50

```

**Note**: Ensure that the input directory contains images in PNG or JPG format for the script to process correctly.
