#yuwana
#6010210712

from grid import Grid

if __name__ == '__main__':
    matrix1 = Grid(3,2)
    matrix2 = Grid(3,2)
    matrix3 = Grid(3,2)

    for row in xrange (matrix1.getHeight()):
        for column in xrange(matrix1.getWidth()):
            matrix1[row][column] = 3*row + 5*column
    print matrix1

    for row in xrange(matrix2.getHeight()):
        for column in xrange(matrix2.getWidth()):
            matrix2[row][column] = 3*row * 5*column
    print matrix2

    for row in xrange(matrix3.getHeight()):
        for col in xrange(matrix3.getWidth()):
            matrix3[row][col] = matrix1[row][col] + matrix2[row][col]
    print matrix3




