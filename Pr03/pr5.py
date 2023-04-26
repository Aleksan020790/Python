a= int (input('a= '))
b= int (input('b= '))
if a>b:
    a,b=b,a
while a<=b:
        if a%2!=0:
            print(a,' ')
        a+=1

