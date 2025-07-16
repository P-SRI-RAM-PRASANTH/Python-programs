#Right angle trinagle
for i in range(1,6):
    for j in range(1,i+1):
        print( "*",end=" ")
    print()
print()
#inverse right angle triangle
for i in range(1,6):
    for j in range(5,i-1,-1):
        print( "*",end=" ")
    print()
print()
# Hollow right angle triangle
for i in range(1,6):
    for j in range(1,i+1):
        if j==1 or j==i or i==5 :
            print("*", end=" ")
        else:
            print(" ", end =" ")
    print()
print()
#square
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
print()

#hollow Square
for i in range(1,6):
    for j in range(1,6):
        if i==1 or j==1 or i==5 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()
# Parellgram
l=3
for i in range(1,5):
    print(" "*l,end=" ")
    for j in range(1,5):
        print("*",end=" ")
    l-=1
    print()
print()
l=0
for i in range(1,6):
    print(" "*l,end=" ")
    for j in range(1,6):
        print("*",end=" ")
    l+=1
    print()
print()
l=0
for i in range(1,6):
    print(" "*l,end=" ")
    for j in range(1,6):
        if j==1 or i==5 or j==5 or i==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    l+=1
    print()
