class BankAccount: 

    def __init__(self, accNo, owner_name, balance):

        self._accNo = accNo
        self.owner_name = owner_name
        self.balance = balance

    # Getter Balance Method
    @property
    def balance(self):
        return self.balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.balance = value

    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount): 
        if amount > self.balance:
            raise ValueError ("Insufficient Balance")
        self.balance -= amount


