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

abiHDFC = BankAccount("hdfc1234", "Abishek", 102)
# print("Balance : ", abiHDFC.balance)
abiHDFC.deposit(1000)
print(abiHDFC.balance)
abiHDFC.withdraw(1102)
print(abiHDFC)
abiHDFC.withdraw(100)