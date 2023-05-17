# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.

def square(side, symbol, peremennaya):  
    for i in range(side):
        for j in range(side):
            if peremennaya or i == 0 or j == 0 or i == side - 1 or j == side - 1:
                print(symbol, end=' ')
            else:
                print(' ', end='')
print()
square(4, '*', True)
square(4, '*', False)

