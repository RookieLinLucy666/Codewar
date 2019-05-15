def find_short(s):
    str_list = s.split()
    length = len(str_list)
    l = len(str_list[0])
    for index in range(1,length):
        list_l = len(str_list[index])
        if list_l <= l:
            l, list_l = list_l, l
    return l # l: shortest word length
print(find_short('this is a happy day'))