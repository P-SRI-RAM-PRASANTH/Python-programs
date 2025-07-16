import threading
def print_numbers():
    b=[3,4,6,7,8]
    for i in b:
        print(i ,end=" ")
thread1=threading.Thread(target=print_numbers())
thread2=threading.Thread(target=print_numbers())
thread3=threading.Thread(target=print_numbers())
thread1.start()
thread2.start()
thread3.start()
