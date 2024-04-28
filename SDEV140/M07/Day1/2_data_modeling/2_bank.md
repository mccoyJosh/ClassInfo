
# Representing a bank (bank class and account class)
In this next example, we represent a bank and the accounts within.
Here we can see how might a class we made can be utilized from within another class


```python
class Account:
    def __init__(self, name, account_num):
        self.__name = name
        self.__account_num = account_num
        self.__balance = 0
        self.__history = []

    def name(self):
        return self.__name

    def account_num(self):
        return self.__account_num

    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount >= 0:
            self.__history.append(amount)
            self.__balance += amount

    def withdraw(self, amount):
        if amount >= 0:
            self.__history.append(amount * -1)
            self.__balance -= amount

    def __str__(self):
        return f'ACCOUNT: {self.__account_num}\n\tName: {self.__name} Amount: {self.__balance}\n\tHistory: {', '.join(map(lambda x: str(x), self.__history))}'


class Bank:
    def __init__(self):
        self.__accounts = []

    def create_account(self, name):
        account_num = 'B' + str(len(self.__accounts))
        acc = Account(name, account_num)
        self.__accounts.append(acc)

    def deposit_account(self, account_id, amount):
        self.__accounts[account_id].deposit(amount)

    def withdraw_account(self, account_id, amount):
        self.__accounts[account_id].withdraw(amount)

    def print_all_account(self):
        for a in self.__accounts:
            print("\n-----------------------------")
            print(a)
        print('\n-------------END-------------')


a_bank = Bank()
a_bank.create_account('Jimmy B')
a_bank.create_account('Bithmew H')
a_bank.create_account('Leo L')

a_bank.deposit_account(0, 1000)
a_bank.deposit_account(0, 200)
a_bank.withdraw_account(0, 700)

a_bank.withdraw_account(1, 1000)
a_bank.withdraw_account(1, 2000)

a_bank.deposit_account(2, 1000)
a_bank.deposit_account(2, 77)

a_bank.print_all_account()
```

