def parse_int(string):
    dict_num = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,"thirteen":13,"fourteen":14,"fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,
    "twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90,"twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90}
    dict_unit = {"hundred":100, "thousand":1000, "million":1000000}
    result = 0
    result1 = 0
    and_count = string.count("and")
    other_count = string.count("-")
    if and_count > 0:
        string = string.replace(" and", "")
    if other_count > 0:
        string = string.replace("-"," ")
    space = string.count(" ")
    if space == 0:
        return dict_num[string]
    for letter in string.split():
        if letter in dict_unit.keys():
            result *= dict_unit[letter]
            if result >= 1000:
                result1 = result
                result = 0
        else:
            result += dict_num[letter]
    return result + result1