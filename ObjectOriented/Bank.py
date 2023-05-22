# Import ABC and abstractmethod from the module abc (which stands for abstract base classes)
from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self, name, location):
        self.name = name
        self.location = location
    @abstractmethod
    def welcome(self):
        pass
    @abstractmethod
    def printBalance():
        pass


class SwissBank(Bank):
    balance = 1000
    def __init__(self, name, location):
        super().__init__(name, location)
    def welcome(self):
        return f"Welcome to {self.name}"
    def printBalance(self):
        return f"Your current balance is {self.balance}"
    def withdraw(self, amount):
        return self.balance - amount



class NepalBank(Bank):
    balance = 2000
    def __init__(self, name, location):
        super().__init__(name, location)
    def welcome(self):
        return f"Welcome to {self.name}"
    def printBalance(self):
        return f"Your current balance is {self.balance}"
    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

def main():
    b = SwissBank("BOS", "Switzerland")
    nb = SwissBank("BON", "Nepal")
    print(b.welcome())
    print(b.printBalance())
    print(nb.welcome())
    print(nb.printBalance())
    print(nb.withdraw(100))
    print(b.printBalance())

if __name__ == "__main__":
    main()