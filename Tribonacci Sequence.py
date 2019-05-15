def tribonacci(signature, n):
    if n == 0:
        return []
    elif n <= 3:
        result = []
        for index in range(n):
            result.append(signature[index])
        return result
    elif n < 0:
        return
    else:
        result = [signature[0],signature[1],signature[2]]
        for index in range(3,n):
            result.append(result[index - 1] + result[index - 2] + result[index - 3])
        return result

print(tribonacci([1,1,1],10))