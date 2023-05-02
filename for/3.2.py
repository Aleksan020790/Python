count = 0
count_= 0
for i in range(100, 1000):
   a= i % 10
   i//= 10
   b= i % 10
   i//= 10
   c= i 
   if a==b or a==c or b==c:
      count+=1
   else:
      count_+=1
print("Кількість чисел де дві однакові цифри в діапазоні: 100-999",count)
   
