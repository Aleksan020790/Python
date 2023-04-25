number= float (input('Внесіть число для піднесення в степінь:' ))
degree =int (input('Внесіть степінь від 0 до 7:'))
if degree < 0 or degree >7:
    print('error')
else:
    print(number, '**', degree,'=', number**degree)
