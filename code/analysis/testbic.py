import multiprocessing

def funSquare(num):
    return num ** 2

if __name__ == '__main__':
    pool = multiprocessing.Pool(2)
    results = pool.map(funSquare, range(8))
    print(results)