def discounted(price, discount, max_discount=50):
    price = abs(float(price))
    discount = abs(float(discount))
    if max_discount > 99:
        raise ValueError('Максимальная скидка не может быть больше 99%')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - price * discount / 100
    return price_with_discount


product = {'name': 'Xiaomi', 'stock': 5, 'price': 65000.0, 'discount': 79}

product['with_discount'] = discounted(
    product['price'], product['discount'], max_discount=80)

print(product)
