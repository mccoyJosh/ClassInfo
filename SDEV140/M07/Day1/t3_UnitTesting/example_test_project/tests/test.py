import unittest
from SDEV140.M07.Day1.t3_UnitTesting.example_test_project.src.file import Bank, Account


class TestBank(unittest.TestCase):
    def test_add_account(self):
        test_bank = Bank()
        test_bank.create_account('Bingo B')
        a = Account('Bingo B', 'B0')
        self.assertEqual(a.balance(), test_bank.get_account(0).balance())

    def test_deposit_account(self):
        test_bank = Bank()
        test_bank.create_account('Bingo B')
        test_bank.deposit_account(0, 1000)
        self.assertEqual(1000, test_bank.get_account(0).balance())

    def test_withdraw_account(self):
        test_bank = Bank()
        test_bank.create_account('Bingo B')
        test_bank.withdraw_account(0, 1000)
        self.assertEqual(-1000, test_bank.get_account(0).balance())

    def test_withdraw_account_2(self):
        test_bank = Bank()
        test_bank.create_account('Bingo B')
        test_bank.withdraw_account(0, -1000)
        self.assertEqual(1000, test_bank.get_account(0).balance())
