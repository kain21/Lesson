def discount(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    print(price_with_discount)


discount(100, 150)
discount(200, -30)
discount(-500, 20)
