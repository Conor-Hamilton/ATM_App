from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_holder, pin, account_type, balance):
        self.account_holder = account_holder
        self.pin = pin
        self.balance = balance
        self.account_type = account_type

    def deposit(self, pin, amount):
        if not self._verify_pin(pin):
            raise ValueError("Invalid pin. Transaction failed")

        if amount <= 0:
            raise ValueError("Invalid amount. Transaction failed")

        self.balance += amount

        print(f"Deposited £{amount} to account {self.account_holder}. New balance is £{self.balance}")
        


    def withdraw(self, pin, amount):
        if not self._verify_pin(pin):
            raise ValueError("Invalid pin. Transaction failed")
        
        if amount <= 0:
            raise ValueError("Invalid amount. Transaction failed")
        
        if amount > self.balance: 
            raise ValueError("Insufficient funds. Transaction failed")
        
        self.balance -= amount

        print(f"Withdrew £{amount} from {self.account_type} account {self.account_holder}. New balance is £{self.balance}")




    def check_balance(self, pin):
        if not self._verify_pin(pin):
            raise ValueError("Invalid pin. Transaction failed")

    # Returns the balance of the account if pin is correct

        pass

    def _verify_pin(self, pin):
        return pin == self.pin
    
    # Verifies the pin by cross-checking with the account's current pin
    

     