from multiprocessing import Process
import os
import time

def info(title):
        print(title)
        print('module name:',  __name__)
        print('parent process:', os.getppid())
        print('process id', os.getpid())
        time.sleep(10)

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('main line')
    processes = []
    for _ in range(10):
        p = Process(target=f, args=('bob',))
        p.start()

    for p in processes:
        p.join()