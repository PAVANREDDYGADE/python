def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

a = 56
b = 98
result = gcd(a, b)
print(result)
