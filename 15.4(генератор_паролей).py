from random import *
print('Добро пожаловать в генератор паролей')

digits = '0123456789'
lowercase_letters = 'bcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
similar = 'il1Lo0O'

chars = ''
quantity = int(input('Сколько паролей делаем? '))
len_pass = int(input('Сколько будет символов в пароле? '))
if_dig = input('В пароле будут числа?("да" / "нет") ')
if_low = input('В пароле будут маленькие буквы?("да" / "нет") ')
if_upp = input('В пароле будут большие буквы?("да" / "нет") ')
if_punct = input('В пароле будут символы?("да" / "нет") ')
if_sim = input('В пароле будут неоднозначные символы "il1Lo0O"?("да" / "нет") ')

if if_dig == 'да':
    chars += digits
if if_low == 'да':
    chars += lowercase_letters
if if_upp == 'да':
    chars += uppercase_letters
if if_punct == 'да':
    chars += punctuation
if if_sim == 'нет':
    for c in similar:
        chars = chars.replace(c, '')

def generate_password(len_pass, chars):
    password = ''
    for i in range(1, quantity+1):
        shuffle(chars)
        sample(chars, len_pass)
        return password

for i in range(quantity):
    generate_password(len_pass, chars)





