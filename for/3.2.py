a= count=0
for i in range (100,1000):
    if str(i)[0]==str(i)[1]==str(i)[2]:
        count=+1
        break
print(count)