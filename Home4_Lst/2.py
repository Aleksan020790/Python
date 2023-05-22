# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран.

import random

pozitiv=0
negativ=0
zero=0
a=[]
for i in range(20):
    a.append(random.randint(-10,20))
    print((a[i]),end=" ")

min_el= min(a)
max_el= max(a)

if a[i]>0:
     pozitiv+=1
elif a[i]<0:
    negativ+=1
elif a [i]==0:
    zero+=1 
print("Позитивних чисел:" ,pozitiv)
print("Негативних чисел:",negativ)
print("Чисела які дорівнюють нулю:",zero)
print("min=",min_el)
print("max=",max_el)


