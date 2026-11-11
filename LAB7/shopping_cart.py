import re

ZONES = {
    "1": "North", "2": "North",
    "3": "West", "4": "West",
    "5": "South", "6": "South",
    "7": "East", "8": "East"
}


def cart_total(cart):
    if not isinstance(cart, str) or not cart.strip():
        raise ValueError("Invalid cart input")

    total = 0

    for item in cart.split(","):
        item = item.strip()

        if not item or item.count(":") != 1:
            raise ValueError("Invalid cart item")

        name, rest = item.split(":")

        if not name.strip() or rest.count("x") != 1:
            raise ValueError("Invalid cart item")

        price, qty = rest.split("x")

        if not price.strip().isdigit() or not qty.strip().isdigit():
            raise ValueError("Price and quantity must be numbers")

        price = int(price.strip())
        qty = int(qty.strip())

        if qty <= 0:
            raise ValueError("Quantity must be positive")

        total += price * qty

    return total


def promo_percent(code):
    if not isinstance(code, str):
        raise ValueError("Invalid promo code")

    code = code.strip().upper()

    if not re.fullmatch(r"OFF(?:100|[0-9]{1,2})", code):
        raise ValueError("Invalid promo code")

    return int(code[3:])


def delivery_zone(pincode):
    if not isinstance(pincode, str):
        raise ValueError("Invalid pincode")

    if not re.fullmatch(r"[0-9]{6}", pincode):
        raise ValueError("Pincode must contain 6 digits")

    zone = ZONES.get(pincode[0])

    if zone is None:
        raise ValueError("Invalid pincode")

    return zone


def main():
    print("==== Running cart_total ====")
    user_input = input(
        "Enter cart as name:pricexqty CSV (e.g. pen:10x2,book:250x1): "
    )

    try:
        print("Cart Total:", cart_total(user_input))
    except ValueError as error:
        print("Invalid cart:", error)

    print("\n==== Running promo_percent ====")
    user_input = input("Enter a promo code (e.g. OFF20): ")

    try:
        print("Discount Percent:", promo_percent(user_input))
    except ValueError as error:
        print("Invalid promo code:", error)

    print("\n==== Running delivery_zone ====")
    user_input = input("Enter a 6 digit pincode (e.g. 560085): ")

    try:
        print("Delivery Zone:", delivery_zone(user_input))
    except ValueError as error:
        print("Invalid pincode:", error)


if __name__ == "__main__":
    main()
