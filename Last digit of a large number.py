#https://www.youtube.com/watch?v=k7rm55Sw-SE
def last_digit(n1, n2):
    if n2 == 0:
        return 1
    dict = {'0':[0],'1':[1],'2':[2,4,8,6],'3':[3,9,7,1],'4':[4,6],'5':[5],'6':[6],'7':[7,9,3,1],'8':[8,4,2,6],'9':[9,1]}
    lastDigitOfN1 = list(str(n1))[-1]
    digits = dict[lastDigitOfN1]
    index = n2 % len(digits)
    return digits[index - 1]