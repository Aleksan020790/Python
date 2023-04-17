a= int (input('input number = '))
b= int (input('input number = '))
c= int (input('input number = '))
print ('Вибір')
print ('1: Максимум із трьох чисел ')
print('2: Мінімум із трьох чисел')
print('3: Середньоарифметичне трьох чисел')
choice =int(input ('Ваш вибір : '))
if choice ==1:
    if a<b>c:
        print( b, 'максимальне число')
    elif b<a>c:
         print( a, 'максимальне число')
    elif a<c>b:
         print( c, 'максимальне число')
    else:
        print('ваші числа дорівнюють один одному')
elif choice ==2:
    if a>b<c:
        print(b, 'мінімальне число')
    elif b>a<c:
        print(a, 'мінімальне число')
    elif a>c<b:
        print(c, 'мінімальне число')
    else:
        print('ваші числа дорівнюють один одному')
elif choice ==3:
    print((a+ b+ c)//3)
else:
    print('error')