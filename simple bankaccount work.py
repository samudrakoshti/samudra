class bankaccount:
    def __init__(self,balance):
        self.__balance=balance
    def check_balance(self):
        print(f"balence={self.__balance}")
    def deposit(self,ammount):
        self.__balance+=ammount
        print(f"ammount successfully deposited in your account:\n updated balence={self.__balance}")
        return self.__balance
    def withdraw(self,ammount):
        if ammount>=self.__balance:
            print("suficient amount not available in your account")
            return
        self.__balance-=ammount
        print(f"withdraw succesful-remening balance={self.__balance}")
database=[{ "name":"samudra","acc_no":1706,"balance":1000,"pin_code":1706},
{    "name":"sagar","acc_no":1708,"balance":2000,"pin_code":1707},
{    "name":"ravi","acc_no":1710,"balance":20000,"pin_code":1708},
{    "name":"raam","acc_no":1712,"balance":200,"pin_code":1709},
{    "name":"rachita","acc_no":1714,"balance":20,"pin_code":1710}]
print(len(database))
def main_account(account):
    print(f"name={account["name"]}")
    c = bankaccount(account["balance"])
    print(" 1.CHECK_BALANCE\n 2.DEPOSIT\n 3.WITHDRAW\n 4.EXIT")
    n = int(input("enter an option above: "))
    if n == 1:
         p=int(input("enter your pin_code"))
         if p==account["pin_code"]:
             c.check_balance()
             get_data()
         else:
             print("incorrect pin_code")
    elif n == 2:
        p = int(input("enter your pin_code"))
        if p == account["pin_code"]:
             A = int(input("enter ammount : "))
             c.deposit(A)
             get_data()
        else:
            print("incorrect pin_code")
    elif n == 3:
        p = int(input("enter your pin_code"))

        if p == account["pin_code"]:
             A = int(input("enter ammount : "))
             c.withdraw(A)
             get_data()
        else:
            print("incorrect pin_code")
    elif n == 4:
        print("operation exited.GOOD BY!")
    else:
         print("entered option not valid")
         get_data()
def get_data():
    while(True):
        print(" 1.ACCOUNT DETAILS \n 2.CREATE AN ACCOUNT \n 3.EXIT ")
        no = int(input("enter an option above: "))
        if no==1:
            acc_no=int(input("enter your account number"))
            for account in database:
                    if account["acc_no"]==acc_no:
                        p = int(input("enter pin_code"))
                        if p == account["pin_code"]:
                            main_account(account)
        elif no==2:

             name = input("enter new name: ")
             acc_no = int(input("enter your new account number: "))
             A = int(input("enter  deposit  ammount : "))
             p=int(input("enter new pin_code"))
             c=bankaccount(0)
             d=c.deposit(A)
             i = len(database)
             database.insert(i,{"name":name,"acc_no":acc_no,"balance":d})

             main_account(database[i])
             i+=1
        elif no==3:
            print("---operation exited---")
            break

        else:
            print("----entered option not valid----")
get_data()
