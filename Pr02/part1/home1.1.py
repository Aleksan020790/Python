a= int (input('input number = '))
b= int (input('input number = '))
c= int (input('input number = '))
print ('Вибір')
print ('1: Сумма чисел ')
print('2: Добуток чисел')
choice =int(input ('Ваш вибір : '))
if choice ==1:
    print (a+b+c)
elif choice ==2:
    print(a*b*c)
else:
    print('error')

