# объявление функции
def draw_triangle():
    for i in range(1, 9):
        a = (' ' * (8 - i)) + ('*' * (i + (i -1)))
        print(a)

# основная программа
draw_triangle()  # вызов функции