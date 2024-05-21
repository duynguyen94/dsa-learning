import numpy as np


def compute_integral_image(image):
    """
    Compute the integral image for a given 2D image.
    TC: O(m * n)
    SC: O(m * n)

    Args:
    image (2D numpy array): Input image.

    Returns:
    2D numpy array: Integral image.
    """
    rows, cols = image.shape
    integral_image = np.zeros((rows, cols), dtype=np.int32)

    # Fill the integral image
    for i in range(rows):
        for j in range(cols):
            integral_image[i, j] = image[i, j]
            if i > 0:
                integral_image[i, j] += integral_image[i - 1, j]
            if j > 0:
                integral_image[i, j] += integral_image[i, j - 1]
            if i > 0 and j > 0:
                integral_image[i, j] -= integral_image[i - 1, j - 1]

    return integral_image


def get_area_sum(integral_image, top_left, bottom_right):
    """
    Compute the sum of pixel values within a given rectangular area using the integral image.
    # TC: O(1)
    # SC: O(1)

    Args:
    integral_image (2D numpy array): Integral image.
    top_left (tuple): Coordinates of the top-left corner of the rectangle (row, col).
    bottom_right (tuple): Coordinates of the bottom-right corner of the rectangle (row, col).

    Returns:
    int: Sum of the pixel values within the specified area.
    """
    row1, col1 = top_left
    row2, col2 = bottom_right

    total = integral_image[row2, col2]

    if row1 > 0:
        total -= integral_image[row1 - 1, col2]
    if col1 > 0:
        total -= integral_image[row2, col1 - 1]
    if row1 > 0 and col1 > 0:
        total += integral_image[row1 - 1, col1 - 1]

    return total


# Example image
image = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Compute the integral image
integral_image = compute_integral_image(image)
print("Integral Image:")
print(integral_image)

# Define the area (top-left and bottom-right coordinates)
top_left = (1, 1)
bottom_right = (2, 2)

# Compute the sum of the area using the integral image
area_sum = get_area_sum(integral_image, top_left, bottom_right)
print(f"\nSum of the area from {top_left} to {bottom_right}: {area_sum}")

