# Напишите функцию, вычисляющую произведение
# элементов списка целых. Список передаётся в качестве параметра. Полученный результат возвращается из функции.
def multiply(x):
    proizvid=1
    for element in x:
        if element!=0:
            proizvid*=element
    return proizvid
a=[3,10]
print(multiply(a))
