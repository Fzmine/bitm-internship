class SBI:
    def __init__(self, name, mob_no, age):
        self.details = {
            "Acc_holder_name": name,
            "Mob_no": mob_no,
            "Age": age,
            "balance": 0
        }

    def deposit(self, amt):
        self.details["balance"] += amt

    def withdraw(self, amt):
        if self.details["balance"] >= amt:
            self.details["balance"] -= amt
            return "sufficient balance"
        else:
            print("insufficient balance")
            return "insufficient balance"

    def transfer(self, sender_acc, amt):
        transfer_condition = sender_acc.withdraw(amt)
        if transfer_condition == "sufficient balance":
            self.deposit(amt)

    def print_balance(self):
        print(self.details["balance"])


yesh_acc = SBI("YESH", "9353363965", "27")
bitm_acc = SBI("BITM", "9885654551", "68")
yesh_acc.deposit(1070000)
bitm_acc.deposit(150000000)
yesh_acc.withdraw(7000)
print(yesh_acc.details["balance"])
print(bitm_acc.details["balance"])
yesh_acc.transfer(bitm_acc, 100000)
print(yesh_acc.details["balance"])
print(bitm_acc.details["balance"])
