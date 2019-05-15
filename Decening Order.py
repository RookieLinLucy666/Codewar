def Descending_Order(num):
    str_num = str(num)
    list_num = list(str_num)
    sort_list_num = sorted(list_num)
    sort_list_num.reverse()
    result = int("".join(sort_list_num))
    return result

print(Descending_Order(1254859723)) #9875543221