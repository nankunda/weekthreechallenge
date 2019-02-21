class BankAccount:
    def __init__(self):
        self.balance = 0
        self.status = False

    def get_balance(self):
        if not self.status:
            raise ValueError(
                "  ohh sorry, its not possible to transact on a closed account")
        return self.balance

    def open(self):
        self.status = True

    def deposit(self, amount):
        if not self.status:
            raise ValueError(
                "  ohh sorry, its not possible to transact on a closed account")
        if amount < 0:
            raise ValueError("amount can not be a negative")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if not self.status:
            raise ValueError(
                "  ohh sorry, its not possible to transact on a closed account")
        if amount < 0:
            raise ValueError("amount can not be a negative")
        if amount > self.get_balance():
            raise ValueError("can not withdraw more than deposited")
        self.balance -= amount
        return self.balance

    def close(self):
        self.status = False