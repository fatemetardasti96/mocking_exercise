from unittest.mock import Mock, patch

from src.e_commerce import ShoppingCart


def test_add_item():
    catalog = Mock()
    catalog.get_product_price.return_value = 100
    
    cart = ShoppingCart(product_catalog=catalog, discount_service=Mock())
    cart.add_item(product_id=10, quantity=2)
    
    assert len(cart.items) == 1
    
    assert cart.items[0]["product_id"] == 10
    assert cart.items[0]["quantity"] == 2
    
    
def test_calculate_total_price():
    items = [{"product_id": 10, "quantity": 2, "price": 100},
             {"product_id": 11, "quantity": 3, "price": 100}]
    
    cart = ShoppingCart(product_catalog=Mock(), discount_service=Mock())
    cart.items = items
    
    assert cart.calculate_total_price() == 500