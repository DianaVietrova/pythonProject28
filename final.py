import uuid
import datetime

class Client:
    def __init__(self, client_id, name, password):
        self.client_id = client_id
        self.name = name
        self.password = password

class Account:
    def __init__(self, account_id, client, balance=0):
        self.account_id = account_id
        self.client = client
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"депозит на {amount} грн")
            print(f"депозит на {amount} грн выполнен успешно. Новый баланс: {self.balance} грн")
        else:
            print("неверная сумма для депозита.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"снятие на {amount} грн")
            print(f"снятие на {amount} грн выполнено успешно. Новый баланс: {self.balance} грн")
        else:
            print("Недостаточная сумма для снятия")

class SavingsAccount(Account):
    def __init__(self, account_id, client, balance=0, interest_rate=0.02):
        super().__init__(account_id, client, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append(f"проценты: {interest} грн")

class CheckingAccount(Account):
    def __init__(self, account_id, client, balance=0, overdraft_limit=300):
        super().__init__(account_id, client, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            self.transactions.append(f"снятие на {amount} грн")
            print(f"снятие на {amount} грн выполнено успешно. Новый баланс: {self.balance} грн")
        else:
            print("Недостаточная сумма для снятия")


client1 = Client(client_id=1, name="Наталья Петренко", password="ello")

savings_account = SavingsAccount(account_id=235, client=client1, balance=5000)
savings_account.deposit(1000)
savings_account.add_interest()

checking_account = CheckingAccount(account_id=236, client=client1, balance=1000)
checking_account.withdraw(2000)

print("транзакции сберегательного аккаунта:", savings_account.transactions)
print("транзакции текущего аккаунта:", checking_account.transactions)
