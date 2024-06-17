import pytest

from proj import *
@pytest.fixture()

def shopping():
    return Shopping()

def test_view_item_list(shopping):
    assert shopping.view()=="success"
# def test_print_bill(shopping):
#     assert shopping.bill() == "no bill"

def test_add_to_cart(shopping):
    assert shopping.add("garlic",2)=="invalid order select from list"

def test_item_need_to_update_is_correctly_entered(shopping):
    assert shopping.update() == "enter the item in the list"

def test_item_need_to_delete_is_correctly_entered(shopping):
    assert shopping.delete() == "enter an order in the list"

def test_unwanted_number_from_list(shopping):
    assert shopping.error()=="enter a valid number"

def test_add_to_cart_success(shopping):
    assert shopping.add("Orange",2) == "success"
    assert shopping.add("Apple",4)=="success"
def test_added_to_list_if_repeated(shopping):
    assert shopping.add("Orange",3)=="enter new item"
def test_update_item(shopping):
    assert shopping.update()=="success"

def test_delete_successfull(shopping):
    assert shopping.delete()=="success"

def test_printbill_sucessfully_terminated(shopping):
    assert shopping.printbill()=="success"
def test_print_bill(shopping):
    assert shopping.bill()=="bill is generated"
