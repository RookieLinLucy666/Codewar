from math import sqrt
def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    divider = 2
    result = False
    while divider <= sqrt(num):
        if(num % divider == 0):
            result = False
            break
        else:
            result = True
            divider += 1
    return result

print(is_prime(11))
