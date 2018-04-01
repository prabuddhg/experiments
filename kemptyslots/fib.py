import time
from numba import jit

@jit
def fib(n):
    if n < 0:
        raise ValueError
    if n < 2:
        return n
    return fib(n-1)+fib(n-2)
 
def fibonacci(n):
    start = time.time()
    res = fib(n)
    end = time.time()
    return res
 
def main():
    start = time.time()
    for i in range(30, 37):
        res = fibonacci(i)
        end = time.time() 
        print("fib(%3d) = %7d (took %0.3fs)" % (i, res, (end-start)))
    end = time.time() 
    print("Total time: %0.3fs" % (end - start)) 
 
if __name__ == "__main__": main()
