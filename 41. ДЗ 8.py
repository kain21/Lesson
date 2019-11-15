def get_summ(one, two, delimiter='&'):
    one = str(one)
    two = str(two)
    one_two = one + delimiter + two
    return one_two


a = get_summ('Learn', 'python')
print(a.upper())
