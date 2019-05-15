def order(sentence):
    dict = {}
    if sentence == "":
        return ""
    list_sentence = sentence.split()
    for arr in list_sentence:
        for index in range(len(arr)):
            if ord(arr[index]) >= 49 and ord(arr[index]) <= 57:
                dict[arr[index]] = arr
                break
    sort_keys = sorted(dict.keys())
    result = []
    for index in range(len(sort_keys)):
        result.append(dict[sort_keys[index]])
    return " ".join(result)

print(order('is2 Thi1s T4est 3a'))