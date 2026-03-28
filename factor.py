def factors(n):
    l1=set()
    for i in range(1,n+1):
        if n%i==0:
            l1.add(i)
    return list(l1)
def prime_factors(n):
    l2=set()
    i=2
    while(i<=n):
        if n%i==0:
            l2.add(i)
            n=n//i
        else:
            i=i+1
    return list(l2)
