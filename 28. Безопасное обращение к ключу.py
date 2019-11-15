product = {
    'name': 'Xiaomi',
    'stock': 5,
    'price': 65000.0
}

# .get() обращается к ключу словаря, если вдруг такого ключа не будет, то выдаст значение None
# применяется чтобы избежать выдачи ошибки в программе
print(product.get('name'))
print(product.get('discount', 10))
