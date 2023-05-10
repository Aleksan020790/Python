# Вывести на экран фигуры, заполненные звездочками.
# Диалог с пользователем реализовать при помощи меню.
# A.
a= '*'
b= " "
choise=input('Введіть ваш вибір:')
if choise=='a':
    for i in range(10):
        for j in range (10):
            if j<i:
                print (b, end=" ")
            else:
                print(a,end="")
        print()
  
 