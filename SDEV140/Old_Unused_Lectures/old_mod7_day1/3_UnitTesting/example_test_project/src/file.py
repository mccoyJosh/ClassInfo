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
        return f'ACCOUNT: {self.__account_num}\n\tName: {self.__name} Amount: {self.__balance}\n\tHistory: {", ".join(map(lambda x: str(x), self.__history))}'


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

    def get_account(self, account_id):
        return self.__accounts[account_id]

    def print_all_account(self):
        for a in self.__accounts:
            print("\n-----------------------------")
            print(a)
        print('\n-------------END-------------')
