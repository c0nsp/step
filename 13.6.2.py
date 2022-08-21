# объявление функции
def get_circle(radius):
    from math import pi
    c = 2*r*pi
    s = pi * r**2
    return c, s

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)