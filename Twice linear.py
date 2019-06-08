def dbl_linear(n):
    u = [1]
    yi, zi = 0, 0
    while len(u) <= n:
        y = 2 * u[yi] + 1
        z = 3 * u[zi] + 1
        if y > z:
            u.append(z)
            zi += 1
        elif y < z:
            u.append(y)
            yi += 1
        else:
            yi += 1 #注意去除重复
    return u[n]

print(dbl_linear(20))