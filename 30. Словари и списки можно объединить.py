phones = ['Xiaomi', 'iPhone XS', 'Samsung', 'OnePlus']

product = {
    'name': 'Xiaomi',
    'stock': 5,
    'price': 65000.0
}

print(product)

product['recomend'] = phones  # добавляем в ключ 'recomend' список phones

print(product)

print(product['recomend'])
print(product['recomend'][1])  # выводит ключ словаря под индексом 1


product['recomend'].append('iPhone 6')  # добавляем в список новый ключ
print(product)
