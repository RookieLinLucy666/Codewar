from math import sqrt
def list_squared(m, n):
    result = []
    for i in range(m, n+1):
        divisorsOfi = []
        for j in range(1,int(sqrt(i))+1):
            if i % j == 0:
                divisorsOfi.append(pow(j, 2))
                if i/j != float(j):
                    divisorsOfi.append(pow(int(i/j),2))
        sumOfDivisorsOfi = 1
        if len(divisorsOfi) > 1:
            sumOfDivisorsOfi = sum(divisorsOfi)
        sqrtSumOfDivisorsOfi = sqrt(sumOfDivisorsOfi)
        if int(sqrtSumOfDivisorsOfi) * int(sqrtSumOfDivisorsOfi) == sumOfDivisorsOfi:
            result.append([i, sumOfDivisorsOfi])
    return result
