a=[2,4,56]
try:
    print(a[6])
except IndexError:
    print("Index is out of Range")