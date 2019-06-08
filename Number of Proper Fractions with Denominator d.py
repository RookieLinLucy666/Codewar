#欧拉函数
from math import sqrt
def proper_fractions(n):
    if n == 1:
        return 0
    res, a = n, n
    for i in range(2, int(sqrt(a)+1)):
        if a % i == 0:
            res = res / i * (i - 1)
            while a % i == 0:
                a /= i
    if a > 1:
        res = res / a * (a - 1)
    return int(res)

print(proper_fractions(15))

