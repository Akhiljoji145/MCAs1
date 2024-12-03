class Bank:
    def __init__(self,acc_no,name,acc_type,balance):
        self.acc_no=acc_no
        self.name=name
        self.acc_type=acc_type
        self.balance=balance
    def display(self):
        print("account number : ",self.acc_no)
        print("name :",self.name)
        print("account type :",self.acc_type)
        print("balance amount :",self.balance)
acc_no=input("enter the account no : ")
name=input("enter the name : ")
acc_type=input("enter the account current/savings : ")
balance=float(input("enter the depositing amount : "))
account=Bank(acc_no,name,acc_type,balance)
account.display()


