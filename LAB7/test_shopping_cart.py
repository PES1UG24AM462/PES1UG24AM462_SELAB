
from hypothesis import given, strategies as st
from shopping_cart import cart_total, promo_percent, delivery_zone


# FUZZ TEST 1: CART TOTAL

@given(st.one_of(st.text(), st.none()))
def test_cart_total_no_crash(value):
    try:
        result = cart_total(value)
    except ValueError:
        return

    assert isinstance(result, int)
    assert result >= 0


# FUZZ TEST 2: PROMO PERCENT

@given(st.one_of(st.text(), st.none()))
def test_promo_percent_no_crash(value):
    try:
        result = promo_percent(value)
    except ValueError:
        return

    assert isinstance(result, int)
    assert 0 <= result <= 100


# FUZZ TEST 3: DELIVERY ZONE

@given(st.one_of(st.text(), st.none()))
def test_delivery_zone_no_crash(value):
    try:
        result = delivery_zone(value)
    except ValueError:
        return

    assert result in {"North", "South", "East", "West"}


# VALID INPUT TESTS

def test_valid_cart_total():
    assert cart_total("pen:10x2,book:250x1") == 270


def test_valid_promo_percent():
    assert promo_percent("OFF20") == 20


def test_valid_delivery_zone():
    assert delivery_zone("560085") == "South"

