
#2403
#medium

#You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has n accounts numbered from 1 to n. The initial balance of each account is stored in a 0-indexed integer array balance, with the (i + 1)th account having an initial balance of balance[i].

#Execute all the valid transactions. A transaction is valid if:

#The given account number(s) are between 1 and n, and
#The amount of money withdrawn or transferred from is less than or equal to the balance of the account.
#Implement the Bank class:

#Bank(long[] balance) Initializes the object with the 0-indexed integer array balance.
#boolean transfer(int account1, int account2, long money) Transfers money dollars from the account numbered account1 to the account numbered account2. Return true if the transaction was successful, false otherwise.
#boolean deposit(int account, long money) Deposit money dollars into the account numbered account. Return true if the transaction was successful, false otherwise.
#boolean withdraw(int account, long money) Withdraw money dollars from the account numbered account. Return true if the transaction was successful, false otherwise.


#my own solution using python3:

class Bank:

    def __init__(self, balance: List[int]):
        self.b = balance
        self.d = dict()
        for i in range(len(self.b)):
            self.d[i + 1] = balance[i]
     

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.d and account2 in self.d:
            if self.d[account1] >= money:
                self.d[account1] -= money
                self.d[account2] += money
                return True
            else:
                return False
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if account in self.d:
            self.d[account] += money
            return True
        else:
            return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if account in self.d:
            if self.d[account] >= money:
                self.d[account] -= money
                return True
            else:
                return False
        else:
            return False
