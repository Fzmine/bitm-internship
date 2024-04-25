class SBI:
    branch_code = 1454
    maintainance_amt =100
    def __init__(self,name,mob_no,age):
        self.Acc_holder_name = name
        self.Mob_no = mob_no
        self.Age = age
        self.balance = 0

    def deposit(self,amt):
        self.balance = self.balance + amt

    def withdraw(self,amt):
        if(self.balance>=amt):
            self.balance = self.balance - amt
        else:
            print("insuffecent balance")

    def transfer(self,sender_acc,amt):
        transfer_condition = sender_acc.withdraw(amt)
        if(transfer_condition == "sufficient balance"):
           self.deposit(amt)

    def print_balance(self):
        print(self.balance)
    @classmethod
    def maintainance_charge(cls,list_acc):
        for every_acc in list_acc:
            every_acc.balance=every_acc.balance - cls.maintainance_amt
    
    @staticmethod
    def thanks_note():
        print("thank you")

yesh_acc=SBI("YESH","9353363965","27")
bitm_acc=SBI("BITM","9885654551","68")
yesh_acc.deposit(1070000)
bitm_acc.deposit(150000000)
yesh_acc.withdraw(7000)
print(yesh_acc.balance)
print(bitm_acc.balance)
print(yesh_acc.balance)
raju_acc=SBI("raju","98765432","16")
yesh_acc.transfer(bitm_acc,100000)
yesh_acc.print_balance()
bitm_acc.print_balance()

