# объявление функции
def convert_to_python_case(text):
    s = txt[0].lower()
    for i in range(1, len(txt)):
        if txt[i].isupper():
            s += '_' + txt[i].lower()
        else:
            s += txt[i]
    return s
    
    
    
            

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))