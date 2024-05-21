import cv2
import numpy as np


def connected_components(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply binary thresholding
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)

    # Perform connected components analysis
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary, connectivity=8)

    # Map component labels to hue values
    label_hue = np.uint8(179 * labels / np.max(labels))
    blank_ch = 255 * np.ones_like(label_hue)
    labeled_image = cv2.merge([label_hue, blank_ch, blank_ch])

    # Convert labeled image to BGR
    labeled_image = cv2.cvtColor(labeled_image, cv2.COLOR_HSV2BGR)

    # Set background label to black
    labeled_image[label_hue == 0] = 0

    return labeled_image, num_labels, labels, stats, centroids


# Example usage
image_path = 'path_to_your_image.png'
labeled_image, num_labels, labels, stats, centroids = connected_components(image_path)

# Display the result
cv2.imshow('Labeled Image', labeled_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(f"Number of labels: {num_labels}")
print(f"Stats: {stats}")
print(f"Centroids: {centroids}")
