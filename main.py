from abc import ABC, abstractmethod

def Account(ABC):
    def __init__(self, account_holder, pin, account_type, balance):
        self.account_holder = account_holder
        self.pin = pin
        self.balance = balance
        self.account_type = account_type

    def deposit(self, pin, amount):
        if not self.pin == pin:
            raise ValueError("Invalid pin. Transaction failed")

        if amount <= 0:
            raise ValueError("Invalid amount. Transaction failed")

        self.balance += amount

        print(f"Deposited £{amount} to account {self.account_holder}. New balance is £{self.balance}")
        



