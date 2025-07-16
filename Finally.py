a=int(input())
try:
    b=100/a
    print(b)
except ZeroDivisionError:
    print("number cant be divided with zero")
finally :
    print("program executed sucessfully..")