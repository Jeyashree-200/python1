def sumof(n,s=0):
    if n==0:
        return 0
    else:
        rem=n%10
        s=s+rem
        return s+sumof(int(n/10))
n=int(input("Enter a no:"))
print("Sum of digits:",sumof(n))
