class BankAccount: 

    def __init__(self, accNo, owner_name, balance):

        self._accNo = accNo
        self.owner_name = owner_name
        if balance < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = balance

    # Getter Balance Method
    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Denominations cannot be 0 or negative")
        self._balance += amount
    
    def withdraw(self, amount): 
        if amount > self.balance:
            raise ValueError ("Insufficient Balance. Current Balance: ", self.balance)
        self._balance -= amount
    
    def __str__(self):
        return f"Account No. : {self._accNo}\nName of Customer: {self.owner_name}\nBalance : {self.balance}"

class SavingsAccount(BankAccount):

    def __init__(self, accNo, owner_name, balance, interest_rate):
        super().__init__(accNo, owner_name, balance)
        self.interest_rate = interest_rate

    def CalculateInterest(self):
        self.interest_rate = self.interest_rate/100
        annual_interest = self.balance * self.interest_rate
        return annual_interest
    
class CurrentAccount(BankAccount):

    def __init__(self, accNo, owner_name, balance, over_draft_limit):
        super().__init__(accNo, owner_name, balance)
        self.over_draft_limit = over_draft_limit
    
    def withdraw(self, amount):
        if amount > self.over_draft_limit + self.balance:
            raise Exception
        self._balance -= amount
        

    
# abiHDFC = BankAccount("hdfc1234", "Abishek", 102)
# # print("Balance : ", abiHDFC.balance)
# abiHDFC.deposit(1000)
# print(abiHDFC.balance)
# abiHDFC.withdraw(1102)
# print(abiHDFC)
# abiHDFC.withdraw(100)

abisavings = SavingsAccount("accabi1234", "Abishek", 1000, 6.5)
print(abisavings.balance)
print(abisavings.interest_rate)
print(abisavings.CalculateInterest())

# abicurrent = CurrentAccount("accabi1234", "Abishek", 1000, 1500)
# print(abicurrent.over_draft_limit)
# print(abicurrent.balance)
# abicurrent.withdraw(2501)
# print(abicurrent.balance)
