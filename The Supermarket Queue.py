def queue_time(customers, n):
    result = [0 for i in range(n)]
    for index in range(len(customers)):
        result[0] += customers[index]
        result.sort()
    return result[n - 1]

print(queue_time([2,2,3,3,4,4],2))