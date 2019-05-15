def likes(names):
    message = ''
    if(len(names) == 0):
        message = 'no one likes this'
    elif(len(names) > 0 and len(names) <= 1):
        message = names[0]+' likes this'
    elif(len(names) > 1 and len(names) <= 2):
        message = names[0]+' and '+names[1]+' like this'
    elif(len(names) > 2 and len(names) <=3):
        message = names[0] + ', ' + names[1] + ' and ' + names[2] + ' like this'
    else:
        message = names[0] + ', ' + names[1] + ' and ' + str(len(names) - 2) + ' others like this'
    return message

