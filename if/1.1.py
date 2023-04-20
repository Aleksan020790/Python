a= int (input('a= '))
b= int (input('b= '))
if not 1 <=a<=100:
    if a % 3 ==0:
        a= "Fizz"
    if a % 5==0:
        a= "Buzz"
    if a % 3 ==0 and a % 5==0:
        a= "Fizz Buzz"
    if a % 3 !=0 and a % 5!=0:
        print(a) 
        a+=1  
else:
    print('error')
