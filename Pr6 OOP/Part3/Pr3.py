class Argumets:
    count=0
    @staticmethod
    def max(a,b,c,d):
        Argumets.count+=1
        return max(a,b,c,d)
    @staticmethod
    def min(a,b,c,d):
        Argumets.count+=1
        return min(a,b,c,d)
    @staticmethod
    def middle_arithmetic(a,b,c,d):
        Argumets.count+=1
        return (a+b+c+d)/4
    @staticmethod
    def factorial(n):
        Argumets.count+=1 
        fac=1
        for i in range(1,n+1):
            fac*=i
        return fac

arg4=Argumets.factorial(5)
print(arg4)


arg3=Argumets.middle_arithmetic(2,2,2,2)
print(arg3)

arg1=Argumets.max(2,3,4,5)
print(arg1)
arg2=Argumets.min(20,30,40,50)
print(arg2)