# Пользователь вводит с клавиатуры арифметическое
# выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения.
# В нашем примере это 35. Арифметическое выражение
# может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/

number1= float(input('ВВедіть перше число: '))
operation = input("Введіть операцію (+, -, *, /): ")
number2 = float(input("Введіть друге число: "))
if operation == '+':
       result = number1 + number2
elif operation == '-':
       result = number1 - number2
elif operation == '*':
       result = number1 * number2
elif operation == '/':
       result = number1 / number2
else:
    print("Error")  
print("Результат:",result) 