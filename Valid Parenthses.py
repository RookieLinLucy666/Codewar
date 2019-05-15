def is_parentheses(char):
    if char == '(' or char == ')':
        return True
    else:
        return False

def clean_parentheses(string):
    for index in range(len(string)):
        if is_parentheses(string[index]) == False:
            string = string[:index] +'a'+ string[index + 1:]
    new_string = string.replace('a','')
    return list(new_string)

def valid_parentheses(string):
    list_str = clean_parentheses(string)
    list_test = []
    for index in range(len(list_str)):
        if list_str[index] == '(':
            list_test.append('(')
        else:
            if len(list_test) == 0:
                return False
            else:
                compare = list_test.pop()
    if len(list_test) == 0:
        return True
    else:
        return False

print(valid_parentheses('hi(hi)()'))
