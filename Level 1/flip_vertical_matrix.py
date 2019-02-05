ef flip_vertical_axis(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])//2):
            matrix[i][j], matrix[i][len(matrix[i])-1-j] = matrix[i][len(matrix[i])-1-j], matrix[i][j]