count = 0
count_=0
for i in range(100, 10000):
   a= i % 10
   i//= 10
   b= i % 10
   i//= 10
   c= i % 10
   i//= 10
   d= i
if a==b or a==c or a==d or b==c or b==d or c==d:
        count += 1
else:
      count_+=1
print('Кількість чисел з різними цифрми в діапазоні 100-9999:', count)