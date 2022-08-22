# объявление функции
def is_magic(date):
    d = [int(i) for i in date.split('.')]
    if d[0] * d[1] == d[2] % 100:
        return True
    else:
        return False

# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))