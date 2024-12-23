class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            print(f"You have successfully deposited {amount}, your updated balance is {self.__balance}")
        else:
            print("Invalid Input")

    def withdraw(self, amount):
        if amount <= self.__balance and amount >= 0:
            self.__balance -= amount
            print(f"You withdrew {amount}, Your balance now is {self.__balance}")
        elif amount > self.__balance:
            return "You don't have enough balance!"
        else:
            print("Invalid withdraw")

    def display_account_info(self):
        return f"Your account number is {self.__account_number} and your total balance is {self.__balance}"

    def __print_balance(self):
        print(f"Current balance is {self.__balance}")

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_bal):
        self.__balance = new_bal
        return self.__balance


acc = BankAccount("123456789", 9000)

acc.deposit(1000.00)  # Depositing 1000.00
acc.withdraw(5000.69)  # Withdrawing 5000.69
acc.withdraw(5000.98)  # Trying to withdraw more than available
acc.deposit(-25)  # Invalid deposit amount

print(acc.display_account_info())
