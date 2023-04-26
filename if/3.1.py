print('Введіть ціну розмови:')
call_price= int(input('n: '))
print('Оберіть оператора')
print('1. Київстар')
print('2. Лайфсел')
print('3. Вадафон')
operator = int(input('Введіть обраного оператора: '))
if operator ==1:
    call_cost=call_price*1.8
elif operator ==2:
    call_cost=call_price*2
elif operator ==3:
    call_cost=call_price*1.5
else:
    print('error')
print('call cost=',call_cost)
