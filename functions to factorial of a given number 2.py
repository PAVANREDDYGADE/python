def factorial(n):  
    f = 1  
    for i in range(1, n + 1):  
        f = f * i  
    return f

x = factorial(int(input("Enter a number: ")))
print(x)
