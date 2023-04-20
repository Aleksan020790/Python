x = int(input('x = '))
s = 0
max,min = x, x
while x != 7:
   s+=x
   if x > max:
       max = x
   if x < min:
       min = x
   x = int(input('x = '))
print("Максимум:", max)
print("Мінімум:", min)
print("Сумма дорівнює:", s)
if x == 7:
    print('Good bye!')


