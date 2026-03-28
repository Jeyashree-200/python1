def prime_check(n):
    if n<2:
        return 0
    for i in range(2,int(n/2)+1):
        if n%i==0:
            return 0
    return 1
n=int(input('enter number'))
f=0
for i in range(2,n):
    if prime_check(i) and prime_check(n-i):
        print(n,"=",i,"+",(n-i))
        f=1
if not f:
    print("The no cannot be represented by sum of two prime nos")
