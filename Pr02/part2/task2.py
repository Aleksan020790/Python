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
if(f==0 or n):
    print("No")
else:
    f,a=a,f
    e,b=b,e
    res= (f*100000 + e*10000 + d*1000 + c *100 + b*10 + a)
    print("res=", res)
