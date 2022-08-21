def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price - price * discount
        return price

    apply_discount()
    return price


discount_price(300, 22)
print(discount_price)
