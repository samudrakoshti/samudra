n=int(input("ENTER A NUMBER: "))
temp=n
sum=0
while n>0:
    r=n%10
    sum=sum*10+r
    n=int(n/10)
    continue

n=temp
print(f"number {n} after swapping:{sum}")
