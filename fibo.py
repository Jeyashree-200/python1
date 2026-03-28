def fibo(n):
    if n==0 or n==1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
a=int(input("enter no of terms needed"))
print("Fibonacci series of ",a,"is\n")
for i in range(a):
    print(fibo(i),end='')
