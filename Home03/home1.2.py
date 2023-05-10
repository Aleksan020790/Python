a= int (input('a= '))
b= int (input('b= '))
print ('Вибір')
print ('1:Всі числа діапазона')
print('2: Всі числа діапазона в спадающем порядки')
print('3: Всі числа кратні 7')
print('4: Всі числа кратні 5')
choice =int(input ('Ваш вибір : '))
if choice ==1:
    while a <=b:
        print (a, end=' ')
        a+=1
elif choice ==2:
    while a <= b:
        print (b, end=' ')
        b-=1
elif choice ==3:
    while a <= b:
        if a % 7==0:
            print (a, end=' ')
        a+=1
elif choice ==4:
    while a <= b:
        if a % 5==0:
            print (a, end=' ')
        a+=1
    
