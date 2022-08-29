from math import factorial
n = int(input())
b = []
for i in range(n+1):
    b.append (int((factorial(n))/(factorial(i)*factorial(n-i))))
print(b)