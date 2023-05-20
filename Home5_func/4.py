# Напишите функцию, которая возвращает минимальное
# из пяти чисел. Числа передаются в качестве параметров.

def min_of_five(a, b, c, d, e):
   min_number = a
   if b < min_number:
       min_number = b
   if c < min_number:
       min_number = c
   if d < min_number:
       min_number = d
   if e < min_number:
       min_number = e
   return min_number
print(min_of_five(123,1,100,545,321))
