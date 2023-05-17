#  Напишите функцию, вычисляющую сумму элементов
# списка целых. Список передаётся в качестве параметра. 
import random

def sum_elemets(mas):
    return sum(mas)

n = int(input("Введіть розмір списку:"))
mas=[]
for i in range(n):
    mas.append(random.randint(2,10))
print(mas)
print(sum_elemets (mas))
