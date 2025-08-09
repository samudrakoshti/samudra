def fact(n):
    if n==0:
        res=1
    else:
        res=n*fact(n-1)
    return res
i=int(input("enter number to find factorial of number: "))
print(fact(i))
