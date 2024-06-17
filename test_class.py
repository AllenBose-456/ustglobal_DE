import pytest

from  cla import Wallet,InsufficiantAmount

@pytest.fixture
def empty_wallet():
    return Wallet()

@pytest.fixture
def wallet():
    return Wallet(20)

def test(empty_wallet):
    assert empty_wallet.balance==0
def test_Setting_initial_amount(wallet):
    assert wallet.balance==20
def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance==100
def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance==10
def test_wallet_spend_cash_raises_exception_of_insufficient_balance(empty_wallet):
    with pytest.raises(InsufficiantAmount):
        empty_wallet.spend_cash(100)

