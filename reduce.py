import functools
def numbers(x,y):
    return x*y
c=[2,3,4,5]
d=functools.reduce(numbers,c)
print(d)