n = int(input("enter how many rows: "))
i = 1
if n % 2 == 0:
    while i <= n // 2:
        j = 0
        while j < i:
            print("*", end=" ")
            j += 1
        print("\n")
        i += 1
    while i < n:
        j = i
        while j < n:
            print("*", end=" ")
            j += 1
        print("\n")
        i += 1
else:
    while i <= n // 2 + 1:
        j = 0
        while j < i:
            print("*", end=" ")
            j += 1
        print("\n")
        i += 1
    while i < n + 1:
        j = i
        while j < n + 1:
            print("*", end=" ")
            j += 1
        print("\n")
        i += 1
