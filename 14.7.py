# объявление функции
def is_pangram(text):
    t = text.lower()
    a = set(t)
    if len(a) == 27:
        return True
    else:
        return False

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))