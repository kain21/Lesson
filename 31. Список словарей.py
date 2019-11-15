stock = [
    {'name': 'Xiaomi', 'stock': 5, 'price': 65000.0, 'recomend': [
        'Xiaomi', 'iPhone XS', 'Samsung', 'OnePlus']},
    {'name': 'iPhone XS', 'stock': 8, 'price': 50000.0, 'discount': 50},
    {'name': 'OnePlus', 'stock': 20, 'price': 38000.0},
]

print(stock[0])

# увеличили ключ 'price' на 10000
stock[0]['price'] = stock[0]['price'] + 10000

# += используется если нужно к этому же значению прибавить 10000
stock[0]['price'] += 10000

# -= используется если нужно из этого же значению вычесть 10000
stock[0]['price'] -= 10000

print(stock[0])
