def sqrt(x, tolerance=1e-10, max_iterations=1000):
    # Method Newton-Raphson method
    # TC: O(logn)
    # SC: O(1)
    if x < 0:
        raise ValueError("Cannot compute the square root of a negative number")
    if x == 0:
        return 0

    # Initial guess
    y = x
    iterations = 0

    while True:
        next_y = 0.5 * (y + x / y)
        if abs(y - next_y) < tolerance:
            break
        y = next_y
        iterations += 1
        if iterations >= max_iterations:
            break

    return y


# Example usage
result = sqrt(25)
print(f"The square root of 25 is approximately {result}")
