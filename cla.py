class InsufficiantAmount(Exception):
    pass

class Wallet(object):
    def __init__(self,initialamount=0):
        self.balance=initialamount
    def spend_cash(self,amount):
        if self.balance<amount:
            raise InsufficiantAmount('not enough money in {}'.format(amount))
        self.balance-=amount

    def add_cash(self,amount):
        self.balance+=amount