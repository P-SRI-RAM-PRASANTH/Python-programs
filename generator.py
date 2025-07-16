def print_numbers():
    b=[3,4,6,7,8]
    for i in b:
        yield i
c=print_numbers()
for j in c:
    print(j)
