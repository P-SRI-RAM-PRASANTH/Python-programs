#fibonacci Series
a,b=1,1
n=int(input("enter no of fibonacci numbers you want"))
sum=0
for i in range(1,n+1):
    sum=a+b
    a=b
    b=sum
    print(sum)