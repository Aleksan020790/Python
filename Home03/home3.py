a= int (input('a= '))
b= int (input('b= '))
while a <= b:
    if a % 3 ==0:
        i= "Fizz"
    # print(a, end= '')
    if a % 5==0:
        i= "Buzz"
    # print(a, end= '') 
    if a % 3 ==0 and a % 5==0:
        i= "Fizz Buzz"
    # print(a, end= '') 
    if a % 3 !=0 and a % 5!=0:
         i=a
    print(i) 
    a+=1   





