def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    sum_TL_to_BR = 0
    sum_BL_to_TR = 0
    height = len(matrix)

    for i in range(0, height):
        for j in range(0, height):
            if i==j:
                sum_BL_to_TR += matrix[i][j]
            if i+j == height-1:
                sum_BL_to_TR += matrix[i][j]

    return sum_BL_to_TR + sum_TL_to_BR