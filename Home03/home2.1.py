a= int (input('input number = '))
b= int (input('input number = '))
s=0
a0=a
i=0
while a <= b:
    s+=a
    a+=1
    i+=1
    if a % 2 == 0:
        print('Сумма четних чисел',s)
    elif a % 2 != 0:
        print('Сумма нечетних чисел ',s)
    elif a%9 == 0:
        print (i,end=' ')
    print('sr=',s/(b-a0+1))



    
     
    
    