from time import time
def performance(func):
    t1 = time()
    func()
    t2 = time()
    print(f'{t2 - t1} sec')

