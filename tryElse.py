b=int(input())
try:
    a=5/b
    print(a)
except ZeroDivisionError:
    print("Number can't be divisible with zero")
else:
    print("execution completed")
