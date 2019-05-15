from math import sqrt
def list_squared(m, n):
    result = []
    for num in range(m, n + 1):
        divider_sum = 0
        for divider in range(1, num + 1):
            if num % divider == 0:
                divider_sum += divider * divider
        sqrt_sum = sqrt(divider_sum)
        if sqrt_sum % 1 == 0:
            result.append([num, divider_sum])
    return result


print(list_squared(1, 250))