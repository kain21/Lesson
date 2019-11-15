stock = [
    {'name': 'Xiaomi', 'stock': 5, 'price': 65000.0, 'recomend': [
        'Xiaomi', 'iPhone XS', 'Samsung', 'OnePlus']},
    {'name': 'iPhone XS', 'stock': 8, 'price': 50000.0, 'discount': 50},
    {'name': 'OnePlus', 'stock': 20, 'price': 38000.0},
]

print(type(stock))

print(type(stock[0]))

# выводит из ключа recomend значение с индексом 1
print(stock[0]['recomend'][1])
