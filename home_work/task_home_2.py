class MatrixError(Exception):
    pass


class AdditionOfMatricesError(MatrixError):

    def __init__(self, lens_matrix: list):
        self.lens_matrix: list = lens_matrix

    def __str__(self):
        if self.lens_matrix[0] != self.lens_matrix[2] and self.lens_matrix[1] != self.lens_matrix[3]:
            return f"Сторона A первой матрицы == {self.lens_matrix[0]} не ровна стороне A второй матрицы == " \
                   f"{self.lens_matrix[2]} и сторона B первой матрицы == {self.lens_matrix[1]} не ровна " \
                   f"стороне B второй матрицы == {self.lens_matrix[3]}. С такими параметрами матрицы не могут " \
                   f"быть суммированы."
        elif self.lens_matrix[0] != self.lens_matrix[2]:
            return f"Сторона A первой матрицы == {self.lens_matrix[0]} не ровна стороне A второй матрицы == " \
                   f"{self.lens_matrix[2]}. С такими параметрами матрицы не могут быть суммированы."
        else:
            return f"Сторона B первой матрицы == {self.lens_matrix[1]} не ровна стороне B второй матрицы == " \
                   f"{self.lens_matrix[3]}. С такими параметрами матрицы не могут быть суммированы."


class MultiplicationOfMatricesError(MatrixError):

    def __init__(self, lens_matrix: list):
        self.lens_matrix: list = lens_matrix

    def __str__(self):
        return f"Сторона B первой матрицы == {self.lens_matrix[0]} не ровна стороне A второй матрицы == " \
               f"{self.lens_matrix[1]}.\nС такими параметрами матрицы не могут " \
               f"быть перемножены.\nСторона B первой должна быть ровна стороне A второй."


class Matrix:
    """An instance of this class stores 1 matrix in memory, performs operations with other instances"""
    def __init__(self, matrix):
        """The matrix is initialized by a property of this class"""
        self.matrix = matrix

    def __str__(self):
        """Displays the string representation of the matrix"""
        string_representation = ''
        for i in self.matrix:
            string_representation += str(i) + '\n'
        return 'It`s matrix\n' + string_representation

    def __repr__(self):
        """String representation of the current instance"""
        return f'Matrix({str(self.matrix)})'

    def matrix_size(self):
        """Calculates the size of the matrix"""
        return len(self.matrix) * len(self.matrix[0])

    def __add__(self, other):
        """Performs matrix addition"""
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in
                            range(len(self.matrix[0]))] for i in range(len(self.matrix))])
        raise AdditionOfMatricesError([len(self.matrix), len(self.matrix[0]), len(other.matrix), len(other.matrix[0])])

    def __mul__(self, other):
        """Performs the product of matrices"""
        if len(self.matrix[0]) == len(other.matrix):
            new_mx = [[0 for _ in range(len(other.matrix[0]))] for _ in range(len(self.matrix))]
            for i in range(len(self.matrix)):
                for j in range(len(other.matrix[0])):
                    for y in range(len(self.matrix[0])):
                        new_mx[i][j] += self.matrix[i][y] * other.matrix[y][j]
            return Matrix(new_mx)
        raise MultiplicationOfMatricesError([len(self.matrix[0]), len(other.matrix)])

    def __eq__(self, o) -> bool:
        """Compares matrices (operator: ==)"""
        return self.matrix_size() == o.matrix_size()

    def __ne__(self, o) -> bool:
        """Compares matrices (operator: !=)"""
        return self.matrix_size() != o.matrix_size()

    def __gt__(self, o) -> bool:
        """Compares matrices (operator: >)"""
        return self.matrix_size() > o.matrix_size()

    def __ge__(self, o) -> bool:
        """Compares matrices (operator: <=)"""
        return self.matrix_size() <= o.matrix_size()

    def __lt__(self, o) -> bool:
        """Compares matrices (operator: <)"""
        return self.matrix_size() < o.matrix_size()

    def __le__(self, o) -> bool:
        """Compares matrices (operator: >=)"""
        return self.matrix_size() >= o.matrix_size()


if __name__ == '__main__':
    mx = [[2],
          [5],
          [8]]

    mx_2 = [[1, 2, 3, 4],
            [4, 5, 6, 2]]

    m = Matrix(mx)
    m_2 = Matrix(mx_2)
    m_3 = m * m_2
    print(m_3)

    ''' =>  It`s matrix
            [9, 12, 15, 8]
            [24, 33, 42, 26]
            [39, 54, 69, 44]   '''
