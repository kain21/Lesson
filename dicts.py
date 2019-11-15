person = {'name': 'vasja', 'surname': 'pupkin', 'email': 'test@gmail.com'}

d = dict(name='petr', tel='1234')

tel = person.setdefault('tel', '12345')
print(tel)
print()
print(person)
