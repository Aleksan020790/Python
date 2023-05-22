# Два списка целых заполняются случайными числами.
# Необходимо:
# ■ Сформировать третий список, содержащий элементы
# обоих списков;
# ■ Сформировать третий список, содержащий элементы
# обоих списков без повторений;
# ■ Сформировать третий список, содержащий элементы
# общие для двух списков;
# ■ Сформировать третий список, содержащий только
# уникальные элементы каждого из списков;
# ■ Сформировать третий список, содержащий только
# минимальное и максимальное значение каждого из
# списков.
import random

lst1=random. sample(range(1,100),10)
lst2=random. sample(range(1,100),10)
lst3=lst1+lst2

lst3_unique=list(set(lst3))
lst3_common=list(set([ x for x in lst1 if x in lst2]))
lst1_unique=list(set(lst1)-set(lst2))
lst2_unique=list(set(lst2)-set(lst1))
lst3_unique_each=lst1_unique+ lst2_unique
lst1_min_max=[min(lst1),max(lst1)]
lst2_min_max=[min(lst2),max(lst2)]
lst3_min_max=lst1_min_max+lst2_min_max

print("Список1:", lst1)
print("Список2:", lst2)
print("Список,що містить всі елементи:", lst3)
print("Список,що містить всі унікальні елементи:",lst3_unique)
print("Список,що містить всі спільні елементи:",lst3_common)
print("Список,що містить всі унікальні елементи кожного списку:",lst3_unique_each)
print("Список,що містить мінімальне та макимальне значення кожного списку:",lst3_min_max)