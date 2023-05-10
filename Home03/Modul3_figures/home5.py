# Вывести на экран фигуры, заполненные звездочками.
# Диалог с пользователем реализовать при помощи меню.n= int(input('n='))
# n= int(input('n='))
# for i in range(n):
#  print(" "*i,(n-2*i)*" *" ," *"*i, sep='')
 
a= '*'
b= " "
choise=input('Введіть ваш вибір:')
if choise=='д':
    for i in range(10):
        for j in range (10):
            if j<(9-i):
                print (b, end=" ")
            else:
                if j<=i:
                    print(a,end="")
                else:
                     print(b,end="")
            if j>(9-i):
                 print(b,end="")
            else:
                if j >=i:
                    print(a,end="")
                else:
                    print(b,end="")
        print()
  