a= int (input('a= '))
b= int (input('b= '))
a0 =a
s= 0
i= 0
while a<=b:
    s+=a
    a+=1
    i+=1
print('s=',s)
print('sr=',s/(b-a0+1))
