# Написать рекурсивную функцию, которая выводит N
# звезд в ряд, число N задает пользователь. Проиллюстрируйте работу функции примером.
N = int(input("Введіть число N:"))
def my_star(N):
    if (N!=1):
        my_star(N-1)

    print("*", end="")
my_star(N)     