phones = ['Xiaomi', 'iPhone XS', 'Samsung', 'OnePlus']

print(phones)

del phones[3]  # del - удаляет 3-й элемент в списке
print(phones)

# .remove() удаляет первый встречающийся элемент с таким названием
phones.remove('iPhone XS')
print(phones)
