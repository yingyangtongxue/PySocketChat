from time import sleep
import threading

def active_threads_test():
    while True:
        sleep(8)
        print("Number of active threads: ",threading.active_count())
