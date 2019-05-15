def binary_array_to_number(arr):
    result = 0
    length = len(arr)
    for index in range(length):
        result += pow(2, index) * arr[length - 1]
        length -= 1
    return result

print(binary_array_to_number([1,1,1,1]))#15
