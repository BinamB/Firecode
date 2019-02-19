def rotate_square_image_ccw(matrix):
    length = len(matrix)
    inL = len(matrix[0])
    # transpose
    for i in range(0, length):
        for j in range(i, inL):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    #horizontal 
    for j in range(0, int(round((length)/2))):
        matrix[j], matrix[length-1-j] = matrix[length-1-j], matrix[j]
    return matrix
