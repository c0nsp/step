from random import *
continue_game = 'д'
print('Добро пожаловать в числовую угадайку')

def is_valid(a):
    if a.isdigit() and 1 <= int(a) <= y:
        return True  
    return False


while continue_game == 'д':
    y = int(input('В каких пределах будем играть? от 1 до '))
    youre_atmp = True
    x = randint(1, y)
    c = 0
    while youre_atmp:
        n = input('Введите Ваше число: ')
        if is_valid(n):
            n = int(n)
            if n < x:
                c += 1
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif n > x:
                c += 1
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем! Вам понадобилось', c, 'попыток')
                youre_atmp  = False
        else:
            print(f'А может быть все-таки введем целое число от 1 до {y}?')
    print('Хотите сыграть еще?("д" / "н")')
    continue_game = input()

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
