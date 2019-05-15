def sub_digital_root(digital, root):
    while digital != 0:
        root = root + digital % 10
        digital = digital // 10
    return root

def digital_root(n):
    root = n % 10
    digital = n // 10
    root = sub_digital_root(digital,root)
    if(root // 10 == 0):
        return root
    else:
        return digital_root(root)

print(digital_root(493193))#2
#132189 6