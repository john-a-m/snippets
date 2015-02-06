from multiprocessing import Pool

#must be picklable and can't be in the same module/namespace? as the pool
#(i.e. they must be separated by `if __name__ == '__main__':`)
def worker(n):
    return n * n

if __name__ == '__main__':
    
    p = Pool() #defaults to `multiprocessing.cpu_count()`
    for w in range(10):
        work = range(10)
        print p.map(worker, work)

