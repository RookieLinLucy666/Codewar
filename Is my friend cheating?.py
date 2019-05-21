def removNb(n):
    result = []
    sumOf = n * (n + 1) / 2
    for a in range(1, n+1):
        b = (sumOf - a) / (a + 1.0)
        if b.is_integer() and b <= n:
            result.append((a, int(b)))
    return result

print(removNb(26))