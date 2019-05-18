def determinant(matrix,result = 0):
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2 and len(matrix[0]) == 2:
        result_cur = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return result_cur

    row = list(range(len(matrix)))
    for i in row:
        minor = matrix[:]
        minor = minor[1:]
        height = len(minor)
        for j in range(height):
            minor[j] = minor[j][0:i]+minor[j][i+1:]
        sign = (-1) ** (i % 2)
        sub_det = determinant(minor)
        result += sign * matrix[0][i] * sub_det
    return result

print(determinant([ [2,5,3], [1,-2,-1], [1, 3, 4]]))
