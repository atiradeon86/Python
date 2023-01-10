from multiprocessing import Process
import os
import time

class MyProcess(Process):
    def __init__(self, name):
        self.name = name
        super(MyProcess, self).__init__()

    def run(self):
        self.f(self.name)
        i = 0
        while i < 10:
                i+=1
                time.sleep(1)
    
    def f(self, name):
            info('function f')
            print('hello',name)
    
def info(title):
    print(title)
    print('module name:',  __name__)
    print('parent process:', os.getppid())
    print('process id', os.getpid())

if __name__ == '__main__':
    info('main line')
    processes = []
    for _ in range(10):
        p = MyProcess('bob')
        p.start()
    
    for p in processes:
        p.join()