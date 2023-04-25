a= int (input('input number = '))
b= int (input('input number = '))

summa_parne=0
summa_not_parne=0
summa_9=0
count_parne=0
count_not_parne=0
count_9=0
while a <= b:
    if a % 2 == 0:
        summa_parne+=a 
        count_parne+=1   
    if a % 2 != 0:
        summa_not_parne+=a
        count_not_parne+=1
    if a%9 == 0:
        summa_9+=a
        count_9+=1
    a+=1
print(summa_parne, summa_not_parne, summa_9 )
print ('ser=',summa_parne/count_parne, summa_not_parne/count_not_parne, summa_9/count_9)




    
     
    
    