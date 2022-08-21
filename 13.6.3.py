# объявление функции
def solve(a, b, c):
    d = b**2 - 4 * a *c
    x1 = ((-1 * b) + (sqrt(d))) / (2 * a)
    x2 = ((-1 * b) - (sqrt(d))) / (2 * a)
    if x1 < x2:
        print(x1, x2, sep='\n')
    else:
        print(x2, x1, sep='\n')
    return x1, x2

    
# считываем данные
a, b, c = int(input()), int(input()), int(input())

# вызываем функцию
x1, x2 = solve(a, b, c)
print(x1, x2)
