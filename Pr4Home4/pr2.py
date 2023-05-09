# Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке. Выведите оба
# количества на экран.

line= 'Oleksandra201324'
count_digit =0
count_digit2 =0
for i in line:
    if 'a'<=i<='z' or 'A'<=i<='Z': 
        count_digit +=1
    if '0'<=i<='9':
        count_digit2 +=1
print (count_digit, count_digit2)
