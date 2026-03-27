##this is for python

from langchain.text_splitter import RecursiveCharacterTextSplitter,Language

text = """

class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")

    def display(self):
        print(f"Account Holder: {self.name}")
        print(f"Balance: {self.balance}")


acc = BankAccount("Akshay", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.display()

"""

splitter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 100,
    chunk_overlap = 0
)
result = splitter.split_text(text)

print(result[0])