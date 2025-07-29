##>>>>>PLAYING WITH STRINGS<<<<<
NAME=input("ENTER YOUR FULL NAME: ")
AGE=int(input("ENTER YOUR AGE: "))
print(NAME.lower()," ",NAME.upper()," ",NAME.replace(" ",""))
print(len(NAME))
str=input("enter a string: ")
print(str[0:7:2])                #>>>>SYNTAX IS==VARIABLE(START:END-1:STEP)<<<<
print("\n \n   ")
print("------PLAYING WITH OPERATERS------")
# '''>>>>>PLAYING WITH OPERATERS<<<<''
a = 99
a += 10
b = 45
print(a > b, "\n", a < b, "\n", (a > b) and (a < b), "\n", (a > b) or (a < b), "\n", not (a > b))

print(" ------------SIMPLE LOOP CONCEPTS----------- \n")
#>>>>>SIMPLE LOOP CONCEPT<<<<<<<
for i in range(1,11):            #>>>>for loop<<<<<
    {
        print(i)
    }

if AGE>18:                       #>>if,else condition<<<<
    print(f"{NAME} is adult \n")
else:
    print(f"{NAME} is minor \n")
