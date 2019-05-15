def format_duration(seconds):
    if seconds == 0:
        return "now"
    else:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        y, d = divmod(d, 365)
        result = [y, d, h, m, s]
        title = ['year','day','hour','minute','second']
        sentence = []
        for index in range(len(result)):
            if result[index] == 0:
                continue
            elif result[index] > 0 and result[index] <= 1:
                sentence.append(str(result[index]) + ' ' + title[index])
            else:
                sentence.append(str(result[index]) + ' '+ title[index] + 's')
        if len(sentence) == 1:
            return "".join(sentence)
        else:
            join_sentence = ", ".join(sentence)
            find_and = join_sentence.rindex(',')
            str_join_sentence = list(join_sentence)
            str_join_sentence[find_and] = ' and'
            return "".join(str_join_sentence)

print(format_duration(3662))