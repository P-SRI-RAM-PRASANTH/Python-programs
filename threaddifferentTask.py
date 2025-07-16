import threading
def print_numbers():
    b=[3,4,6]
    for i in b:
        print(i ,end=" ")
def Print_names():
    a=["ram","sai","venky"]
    for i in range(len(a)):
        print(a[i])
thread1=threading.Thread(target=print_numbers)
thread2=threading.Thread(target=Print_names)
thread3=threading.Thread(target=print_numbers)
thread1.start()
thread2.start()
thread3.start()