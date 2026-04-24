from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self,account_no,balance):
        self.account_no = account_no
        self.__balance = balance
    def deposit(self,amount):
        self._Account__balance += amount
        print(f"Deposited: {amount}")
    @abstractmethod
    def withdraw(self,amount):
        pass
    @property
    def get_balance(self):
        return self.__balance
class SavingsAccount(Account):
    def __init__(self,account_no,balance):
        super().__init__(account_no,balance)
    def withdraw(self,amount):
        if self.get_balance -amount<500:
            print("not possible")
        else:
            self._Account__balance -=amount
            print(f"{amount}")
class CurrentAccount(Account):
    def __init__(self,account_no,balance):
        super().__init__(account_no,balance)
    def withdraw(self,amount):
        if self.get_balance-amount < -1000:
            print("lmt exceeded")
        else:
            self._Account__balance -=amount
            print(f"{amount}")

s = SavingsAccount("sbixyz",5000)
c = CurrentAccount("123",600)

s.deposit(500)
s.withdraw(1500)
print("Savings Balance:", s.get_balance)
c.withdraw(1200)
print("Current Balance:", c.get_balance)



