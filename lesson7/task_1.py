class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        return Matrix([list(map(sum, zip(self.matrix[index_row], other.matrix[index_row])))
                       for index_row in range(len(self.matrix))])


matrix_1 = Matrix([[1, 2, 3], [3, 2, 1]])
matrix_2 = Matrix([[2, 3, 4], [4, 3, 2]])

print('Первая матрица')
print(matrix_1)

print('Вторая матрица')
print(matrix_2)

print('Результат сложения')
print(matrix_1 + matrix_2)
