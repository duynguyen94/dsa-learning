class SparseMatrix:
    def __init__(self, shape):
        self.shape = shape
        self.data = []
        self.indices = []
        self.indptr = [0]

    def add_value(self, row, col, value):
        """
        Adds a value to the sparse matrix.
        """
        if value != 0:
            self.data.append(value)
            self.indices.append(col)

            while len(self.indptr) <= row:
                self.indptr.append(len(self.data) - 1)

            self.indptr[row + 1] = len(self.data)

    def to_dense(self):
        """
        Converts the sparse matrix to a dense matrix.
        """
        dense_matrix = [[0] * self.shape[1] for _ in range(self.shape[0])]

        for row in range(self.shape[0]):
            for idx in range(self.indptr[row], self.indptr[row + 1]):
                col = self.indices[idx]
                dense_matrix[row][col] = self.data[idx]

        return dense_matrix

    def __repr__(self):
        dense_matrix = self.to_dense()
        return '\n'.join([' '.join(map(str, row)) for row in dense_matrix])

    def multiply(self, vector):
        """
        Multiplies the sparse matrix with a dense vector.
        """
        if len(vector) != self.shape[1]:
            raise ValueError("Vector length must match the number of columns in the matrix.")

        result = [0] * self.shape[0]

        for row in range(self.shape[0]):
            for idx in range(self.indptr[row], self.indptr[row + 1]):
                col = self.indices[idx]
                result[row] += self.data[idx] * vector[col]

        return result


# Example usage
matrix = SparseMatrix((3, 3))
matrix.add_value(0, 0, 1)
matrix.add_value(0, 2, 2)
matrix.add_value(1, 1, 3)
matrix.add_value(2, 0, 4)
matrix.add_value(2, 2, 5)

print("Sparse Matrix:")
print(matrix)

vector = [1, 2, 3]
result = matrix.multiply(vector)
print("\nResult of multiplication with vector [1, 2, 3]:")
print(result)
