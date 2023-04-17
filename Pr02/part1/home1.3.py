a= int (input('input number = '))
print ('Вибір')
print ('1: Перевести метри в милі ')
print('2: Перевести метри в дюйми')
print('3: Перевести метри в ярди ')
choice =int(input ('Ваш вибір : '))
if choice ==1:
    print(a* 0.000621)
elif choice ==2:
    print(a*39.37)
elif choice ==3:
    print(a*1.094)
else:
    print('error')