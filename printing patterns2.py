n = int(input("enter how many rows: "))
i = 1
while i <= n:
    j = i
    if i % 2 == 0:
        while j <= n:
            print("*", end=" ")
            j += 1
        print("\n")
        i += 1
    else:
        while j <= n:
            print("-", end=" ")
            j += 1
        print("\n")
        i += 1
