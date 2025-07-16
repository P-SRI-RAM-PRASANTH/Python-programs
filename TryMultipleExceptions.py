a=[]
for _ in range(int(input())):
    a.append(_)
print(a)
b=int(input("enter a number to divide with 100"))
i=int(input("Enter an index to access list element: "))
try:
   d=100/b
   print(d)
   print(a[i])
except ZeroDivisionError:
    print("Number can't be divisible with 0 ")
except IndexError:
    print("Index is out of range") 