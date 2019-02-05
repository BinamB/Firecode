def flip_horizontal_axis(matrix):
    res = []
    for i in range(0, len(matrix)-1):
        matrix[i], matrix[len(matrix)-1-i] = matrix[len(matrix)-1-i], matrix[i] 