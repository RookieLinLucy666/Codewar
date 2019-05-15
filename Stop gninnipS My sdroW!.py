def spin_words(sentence):
    # Your code goes here
    list_sentence = sentence.split()
    result = []
    for word in list_sentence:
        if len(word) >= 5:
            result.append(word[::-1])
        else:
            result.append(word)
    return " ".join(result)

print(spin_words("Welcome"))