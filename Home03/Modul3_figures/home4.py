# Вывести на экран фигуры, заполненные звездочками.
# Диалог с пользователем реализовать при помощи меню.n= int(input('n='))
a= '*'
b= " "
choise=input('Введіть ваш вибір:')
if choise=='г':
    for i in range(10):
        for j in range (10):
            if j<(9-i):
                print (b, end=" ")
            else:
                if j<=i:
                    print(a,end="")
                else:
                     print(b,end="")
        print()
  