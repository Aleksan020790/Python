# Пользователь с клавиатуры вводит элементы списка
# целых. Необходимо посчитать сумму всех элементов
# и их среднеарифметическое. Результаты вывести на
# экран.
n= int(input('count of number: '))
lst=[]
for i in range (n):
    lst.append (int(input('number['+str(i)+']=')))
number=int(input('n='))
count=lst.count(number)
print (count)
print(sum(lst))
print(sum(lst)/n)

