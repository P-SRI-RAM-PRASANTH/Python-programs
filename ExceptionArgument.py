a=int(input("Enter a number to divide with 50: "))
try:
    b=50/a
    print(b)
except ZeroDivisionError as e:
    print(e, "is not allowed")