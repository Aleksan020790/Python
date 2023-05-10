a= int(input('Введіть число a= '))
b= int(input('Введіть число b= '))
for i in range (a,b+1):
    for j in range (1,11):
        print(i ,"*",j, "=", i*j, end= ' ')
    print()