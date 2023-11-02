import random

a = random.randint(1,10)
flag_win = 0
for i in range(3):
    guess = input('Введите число! ')
    if guess.isnumeric():
        guess = int(guess)
        if guess == a:
            flag_win = 1
            print(f'Правильно! Вы угадали с {i+1}-й попытки!')
            break
        elif guess < a:
            print('Неправильно, слишком мало!')
        else:
            print('Неправильно, слишком много!')
    else:
        print('Не число! Вы зря потратили попытку.')
    print(f'Осталось попыток:  {2-i}!')
if flag_win == 0:
    print('Вы проиграли!')
