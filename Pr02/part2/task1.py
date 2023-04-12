n= int (input('n= '))
a= n %10
n//=10
print (n)
b= n%10
n//=10
print(n)
c= n%10
n//=10
print (n)
d= n%10
n//=10
print(n)
e= n%10
n//=10
print(n)
f= n%10
n//=10
print(n)
if (f+e+d==c+b+a):
    print("Lucky")
else:
    print("No Lucky")
