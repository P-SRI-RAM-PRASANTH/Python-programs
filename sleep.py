import threading
import time
def print_numbers():
    b=[3,4,6]
    for i in b:
        print(i)
        time.sleep(3)
thread1=threading.Thread(target=print_numbers)
thread2=threading.Thread(target=print_numbers)
thread3=threading.Thread(target=print_numbers)
thread1.start()
thread2.start()
thread3.start()