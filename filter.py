def print_numbers(n):
    return n%2==0
    
b=[3,4,6,7,8]
c=filter(print_numbers,b)
print(list(c))