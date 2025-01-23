n = int(input("Enter the number of terms: "))
a, b = 5,6
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
