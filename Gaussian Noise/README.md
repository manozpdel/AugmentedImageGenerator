**Image Gaussian Noise Addition Script**

**Description:**

This Python script applies Gaussian noise to images using the OpenCV library.

**Usage:**

1. Place the images requiring Gaussian noise addition into the designated input directory (`cats/` in this script).
2. Run the script. It creates a directory named `noisy_images` within the input directory (if it doesn't exist), and it stores the noisy images there.
3. You can adjust the mean and standard deviation parameters for the Gaussian noise by modifying the `mean` and `stddev` variables in the script. The default values are 0 and 50, respectively.

**Requirements:**

- Python 3.x
- OpenCV library (`cv2`)
- NumPy library (`numpy`)

**Example:**

```python
# Define parameters for Gaussian noise
mean = 0
stddev = 50  # Adjust as needed

```

**Note:**

- Ensure the input directory contains images in PNG or JPG format.
- The script overwrites existing files with the same name in the output directory.
