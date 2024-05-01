**Image Shearing Script**

**Description**

This Python script enables the shearing of images using the OpenCV library. It provides a function `shear_image(image, shear_factor_x, shear_factor_y)` to apply shearing transformations to input images. The script traverses through a directory containing images in PNG or JPG format, applies the specified shearing factors to each image, and saves the sheared images in an output directory.

**Usage**

1. Place the images requiring shearing into the designated input directory (cats/ in this script).
2. Execute the script. It generates a directory named sheared_images within the input directory (if it doesn't exist), and it stores the sheared images there.
3. You can adjust the shearing factors by modifying the `shear_factor_x` and `shear_factor_y` variables in the script. The default values are set to 0.2 for `shear_factor_x` and 0.1 for `shear_factor_y`.

**Requirements**

- Python 3.x
- OpenCV library (cv2)
- NumPy library (numpy)

**Example**

```python
# Define shearing factors
shear_factor_x = 0.2  # Adjust as needed
shear_factor_y = 0.1  # Adjust as needed
```

**Note**

- Ensure the input directory contains images in PNG or JPG format.
- The script overwrites existing files with the same name in the output directory.
