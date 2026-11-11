
import pytest

from shopping_cart import item_total, cart_discount, shipping_fee


# ITEM TOTAL - BRANCH COVERAGE

def test_food_category():
    assert item_total("food", 100, 2) == 210


def test_electronics_category():
    assert item_total("electronics", 100, 10) == 1062


def test_clothing_category():
    assert item_total("clothing", 50, 1) == 56


def test_invalid_category():
    with pytest.raises(ValueError):
        item_total("furniture", 100, 2)


def test_negative_price():
    with pytest.raises(ValueError):
        item_total("food", -10, 2)


def test_zero_price():
    assert item_total("food", 0, 1) == 0


def test_zero_quantity():
    with pytest.raises(ValueError):
        item_total("food", 100, 0)


def test_negative_quantity():
    with pytest.raises(ValueError):
        item_total("food", 100, -1)


# CART DISCOUNT - BRANCH COVERAGE

def test_cart_above_5000():
    assert cart_discount(6000, False, None) == 500


def test_cart_exactly_5000():
    assert cart_discount(5000, False, None) == 500


def test_cart_between_2000_and_5000():
    assert cart_discount(3000, False, None) == 200


def test_cart_exactly_2000():
    assert cart_discount(2000, False, None) == 200


def test_cart_below_2000():
    assert cart_discount(1000, False, None) == 0


def test_prime_customer():
    assert cart_discount(500, True, None) == 100


def test_non_prime_customer():
    assert cart_discount(500, False, None) == 0


def test_coupon_applied():
    assert cart_discount(2000, False, "FLAT10") == 400


def test_coupon_below_1000():
    assert cart_discount(500, False, "FLAT10") == 0


def test_invalid_coupon():
    assert cart_discount(2000, False, "INVALID") == 200


# SHIPPING FEE - BRANCH COVERAGE

def test_prime_standard_shipping():
    assert shipping_fee(100, True, False) == 0


def test_prime_express_shipping():
    assert shipping_fee(100, True, True) == 50


def test_non_prime_cart_above_500():
    assert shipping_fee(1000, False, False) == 0


def test_non_prime_cart_exactly_500():
    assert shipping_fee(500, False, False) == 0


def test_non_prime_cart_below_500():
    assert shipping_fee(100, False, False) == 40


def test_non_prime_express_shipping():
    assert shipping_fee(100, False, True) == 140

