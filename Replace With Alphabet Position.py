def alphabet_position(text):
    tran_text = text.lower()
    result = []
    for char in tran_text:
        if ord(char) >= 97 and ord(char) <= 122:
            result.append(str(ord(char) - 96))
    return " ".join(result)


print(alphabet_position("The sunset sets at twelve o' clock."))