def find_outlier(integers):
    odd_count = 0
    even_count = 0
    for index in range(3):
        if integers[index] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if even_count > odd_count:
        for num in integers:
            if num % 2 != 0:
                return num
    else:
        for num in integers:
            if num % 2 == 0:
                return num

print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))