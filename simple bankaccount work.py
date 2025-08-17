class bankaccount:
    def __init__(self,balance):
        self.__balance=balance
    def check_balance(self):
        print(f"balence={self.__balance}")
    def deposit(self,ammount):
        self.__balance+=ammount
        print("ammount successfully deposited in your account:")
        print(f"balence={self.__balance}")
        return self.__balance
    def withdraw(self,ammount):
        if ammount>self.__balance:
            print("suficient amount not available in your account")
            return
        self.__balance-=ammount
        print(f"withdraw succesful-balance={self.__balance}")
database=[{ "name":"samudra","acc_no":1706,"balance":1000},
{    "name":"sagar","acc_no":1708,"balance":2000},
{    "name":"ravi","acc_no":1710,"balance":20000},
{    "name":"raam","acc_no":1712,"balance":200},
{    "name":"rachita","acc_no":1714,"balance":20}]
def main_account(account):
    print(f"name={account["name"]}")
    print(f"balence={account["balance"]}")
    c = bankaccount(account["balance"])
    print("1.checck-balance")
    print("2.deposit")
    print("3.withdraw")
    n = int(input("enter an option above: "))
    if n == 1:
        c.check_balance()
    elif n == 2:
        A = int(input("enter ammount : "))
        c.deposit(A)
    elif n == 3:
        A = int(input("enter ammount : "))
        c.withdraw(A)

    else:
        print("entered option not valid")

print("1.account details")
print("2.creat an account")
no = int(input("enter an option above: "))
if no==1:
     acc_no=int(input("enter your account number"))
     for account in database:
         if account["acc_no"]==acc_no:
             main_account(account)



elif no==2:

     name = input("enter name: ")
     acc_no = int(input("enter account number: "))
     A = int(input("enter deposit a ammount : "))
     c=bankaccount(0)
     d=c.deposit(A)
     dict=[]
     dict.append({"name":name,"acc_no":acc_no,"balance":d})
     main_account(dict[0])
