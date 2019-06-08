from itertools import combinations_with_replacement
def find_all(sum_dig, digs):
    combs = combinations_with_replacement(list(range(1,10)), digs)
    result = [''.join(str(char) for char in list(comb)) for comb in combs if sum(comb) == sum_dig]
    if len(result) == 0:
        return []
    return [len(result),int(result[0]),int(result[-1])]

print(find_all(10,3))