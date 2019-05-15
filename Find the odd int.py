def find_it(seq):
    result = {}
    for index in range(len(seq)):
        result[seq[index]] = seq.count(seq[index])
    for key in result:
        if result[key] % 2 == 0:
            continue
        else:
            return key

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
