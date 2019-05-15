def sub_persistence(n):
    str_n = str(n)
    result = 1
    for index in range(len(str_n)):
        result *= int(str_n[index])
    return result

def persistence(n):
    if n // 10 == 0:
        return 0
    else:
        count = 1
        result = sub_persistence(n)
        while result // 10 != 0:
            result = sub_persistence(result)
            count += 1
        return count


print(persistence(39))#3