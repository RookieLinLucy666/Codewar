class Calculator(object):
    def evaluate(self, string):
        priority = {'-':0,'+':0,'*':1,'/':1}
        laterfix = []
        signal = []
        for char in string.split():
            if char not in priority.keys():
                laterfix.append(float(char))
            else:
                if len(signal) == 0:
                    signal.append(char)
                else:
                    while len(signal) != 0 and priority[signal[-1]] >= priority[char]:
                        laterfix.append(signal.pop())
                    signal.append(char)
        while len(signal) > 0:
            laterfix.append(signal.pop())
        result = []
        for element in laterfix:
            if element not in priority.keys():
                result.append(element)
            else:
                b = result.pop()
                a = result.pop()
                if element == '+':
                    result.append(a+b)
                elif element == '-':
                    result.append(a - b)
                elif element == '*':
                    result.append(a * b)
                elif element == '/':
                    result.append(a / b)

        return  result[0]


print(Calculator().evaluate("2 / 2 + 3 * 4 - 6"))
