import pytest
from main import Checkout

# test basket value with invalid json basket
def test_invalid_item_code_type(): 
    with pytest.raises(TypeError) as excinfo:
        json_basket = '[{"code": 1,"quanity":2},{"code":"B","quanity":1},{"code":"C","quantity":1}]'
        checkout = Checkout(json_basket)
        sub_total = checkout.get_total()
    assert str(excinfo.value) == "Item code must be a string" 

def test_invalid_item_quantity_type(): 
    with pytest.raises(TypeError) as excinfo:
        json_basket = '[{"code":"A","quantity":"two"},{"code":"B","quantity":1},{"code":"C","quantity":"7"}]'
        checkout = Checkout(json_basket)
        sub_total = checkout.get_total()
    assert str(excinfo.value) == "Item quantity must be an integer"
        
def test_invalid_item_code(): 
    with pytest.raises(ValueError) as excinfo:
        json_basket = '[{"code":"F","quantity":2},{"code":"B","quantity":1},{"code":"C","quantity":7}]'
        checkout = Checkout(json_basket)
        sub_total = checkout.get_total()
    assert str(excinfo.value) == "Invalid item code"

def test_invalid_quantity(): 
    with pytest.raises(ValueError) as excinfo:
        json_basket = '[{"code":"A","quantity":-2},{"code":"B","quantity":0},{"code":"C","quantity":7}]'
        checkout = Checkout(json_basket)
        sub_total = checkout.get_total()
    assert str(excinfo.value) == "Item quantity must be greater than 0"

def test_invalid_JSON(): 
    with pytest.raises(TypeError) as excinfo:
        json_basket = '[{code:"A","quantity":2},{"code":B,quantity:1},{"code":"C","quantity":7}]'
        checkout = Checkout(json_basket)
        sub_total = checkout.get_total()
    assert str(excinfo.value) == "Invalid JSON"
    
            

# test checout total without any deals
@pytest.mark.parametrize("test_input,expected", 
    [('[{"code":"A","quantity":2},{"code":"B","quantity":1},{"code":"C","quantity":1},{"code":"D","quantity":1}]', 172), 
     ('[{"code":"A","quantity":2},{"code":"B","quantity":1}]', 135), 
     ('[]', 0),
     ('[{"code":"A","quantity":2}]', 100)
     ])
def test_basic_total(test_input, expected):
    checkout = Checkout(test_input)
    sub_total = checkout.get_total()
    assert sub_total == expected

# test the basic total with deals
@pytest.mark.parametrize("test_input,expected",[
    ('[{"code":"A","quantity":3},{"code":"B","quantity":3},{"code":"C","quantity":1},{"code":"D","quantity":2}]', 284),
    ('[{"code":"A","quantity":2},{"code":"B","quantity":2}]', 160),
    ('[{"code":"A","quantity":7},{"code":"B","quantity":4}]', 450)
])
def test_special_checkout(test_input, expected):
    checkout = Checkout(test_input)
    sub_total = checkout.get_total()
    assert sub_total == expected
    


 