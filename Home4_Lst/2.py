# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчитать количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран.

import random

lst = [random.randint(-20, 30) for _ in range(50)]

min_element = min(lst)

max_element = max(lst)

negative_count = sum(1 for i in lst if i < 0)

positive_count = sum(1 for i in lst if i > 0)

zero_count = sum(1 for i in lst if i == 0)

print("Minimum element:", min_element)

print("Maximum element:", max_element)

print("Negative elements count:", negative_count)

print("Positive elements count:", positive_count)

print("Zero elements count:", zero_count)
