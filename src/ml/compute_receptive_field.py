def compute_receptive_field(strides, kernel_sizes):
    """
    Compute the receptive field for a particular node in a 1-dimensional CNN.

    Args:
    strides (list of int): List of stride values for each convolutional layer.
    kernel_sizes (list of int): List of kernel sizes for each convolutional layer.

    Returns:
    int: The receptive field of a node in the final layer.
    """
    if len(strides) != len(kernel_sizes):
        raise ValueError("The length of strides and kernel_sizes lists must be equal.")

    receptive_field = 1
    for stride, kernel_size in zip(receptive_field):
        receptive_field = receptive_field * stride + (kernel_size - 1)

    return receptive_field

# Example usage
strides = [1, 2, 2]
kernel_sizes = [3, 3, 3]
receptive_field = compute_receptive_field(strides, kernel_sizes)
print(f"The receptive field is: {receptive_field}")
