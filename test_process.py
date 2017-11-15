import multiprocessing
import os

def ren_proc(name):
    print('Run child process %s (%s)...' % (name,os.getpid()))

if __name__ == '__main__':
    print('Parents process %s.' % os.getpid())
    p = multiprocessing.Process(target=ren_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')