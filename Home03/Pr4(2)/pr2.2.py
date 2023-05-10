# Пользователь с клавиатуры вводит элементы списка
# целых и некоторое число. Необходимо посчитать сколько раз данное число присутствует в списке. Результат
# вывести на экран. 
n= int(input('count of number: '))
lst=[]
for i in range (n):
    lst.append (int(input('number['+str(i)+']')))
number=int(input('n='))
count=lst.count(number)
print (count)