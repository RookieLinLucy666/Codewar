def sum_of_intervals(intervals):
    result = []
    for tuples in intervals:
        for indice in range(tuples[0],tuples[1]):
            if indice not in result:
                result.append(indice)
    return len(result)

print(sum_of_intervals([
   [1,5],
   [10, 20],
   [1, 6],
   [16, 19],
   [5, 11]
]))