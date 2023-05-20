# Напишите функцию, которая отображает пустой или
# заполненный квадрат из некоторого символа. Функция
# принимает в качестве параметров: длину стороны квадрата, символ и переменную логического типа:
# ■ если она равна True, квадрат заполненный;
# ■ если False, квадрат пустой.


def print_square(side_length, symbol, filled):

    if filled:
# Заполненный квадрат

        for i in range(side_length):

            print(symbol * side_length)

    else:
# Пустой квадрат

        for i in range(side_length):

            if i == 0 or i == side_length - 1:
# Верхняя и нижняя границы квадрата

                print(symbol * side_length)

        else:
# Стороны квадрата

            print(symbol + " " * (side_length - 2) + symbol)    

# print_square(4, "*", True)

print_square(4, "*", False)


# В этой функции мы используем логическую переменную filled