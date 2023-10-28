class BankAccount:
  def __init__(self, account_number, account_holder, initial_balance=0.0):
      self.__account_number = account_number  # Private attribute
      self.__account_holder = account_holder  # Private attribute
      self.__account_balance = initial_balance  # Private attribute

  def deposit(self, amount):
      if amount > 0:
          self.__account_balance += amount

  def withdraw(self, amount):
      if amount > 0 and amount <= self.__account_balance:
          self.__account_balance -= amount

  def display_balance(self):
      print("Account Number:", self.__account_number)
      print("Account Holder:", self.__account_holder)
      print("Account Balance:", self.__account_balance)

# Create an instance of the BankAccount class
account1 = BankAccount("123456", "John Doe", 1000.0)

# Test deposit and withdrawal functionality
account1.deposit(500)
account1.withdraw(300)
account1.display_balance()
