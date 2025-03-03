from  source.shopping_cart import ShoppingCart
import pytest
def test_can_add_item_to_cart():
    cart = ShoppingCart()
    cart.add("apple")
    assert cart.size() == 1
def test_when_item_added_cart_contains_item():
    cart = ShoppingCart()
    cart.add('apple')
    assert 'apple' in cart.get_items()

def test_when_add_more_tan_max_items_should_fail():
    cart = ShoppingCart(5)
    with pytest.raises(OverflowError):
        for _  in range(6):
            cart.add('apple')
