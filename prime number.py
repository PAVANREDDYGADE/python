n=int(input())
c=0
for i in range(2,n//2):
    if n%2==0:
        c=c+1

        if c==0:
            print(n,"is prime")
            else:
                print(n,"is not prime")
                      
