# объявление функции
import math
def compute_binom(n, k):
    m = n - k
    return math.factorial(n) // (math.factorial(k) * math.factorial(m))

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))