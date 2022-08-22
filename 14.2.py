# объявление функции
def get_shipping_cost(quantity):
    a = 1000
    if n == 1:
        return a
    elif n >= 2:
        a += (n-1) * 120
        return a
         
        

# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))