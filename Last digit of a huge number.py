#https://brilliant.org/wiki/finding-the-last-digit-of-a-power/
#https://www.youtube.com/watch?v=k7rm55Sw-SE
def last_digit(lst):
    if lst == []:
        return 1
    result = 1
    for num in lst[::-1]:
        result = num ** (result if result < 4 else result % 4 + 4)
        print(result)
    return result % 10


print(last_digit([3, 3, 3,4]))