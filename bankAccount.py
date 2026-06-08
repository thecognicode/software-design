class BankAccount: 

    def __init__(self, accNo, owner_name, balance):

        self._accNo = accNo
        self.owner_name = owner_name
        self.balance = balance

    # Getter Balance Method
    @property
    def balance(self):
        return self.balance
    
    
