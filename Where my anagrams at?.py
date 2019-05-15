def anagrams(word, words):
    sort_word = "".join(sorted(word))
    result = []
    for sub_words in words:
        if sort_word == "".join(sorted(sub_words)):
            result.append(sub_words)
        else:
            continue
    return result


print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))