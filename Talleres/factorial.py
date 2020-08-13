//este trabajo fue hecho por Salomon Velez y Juan Manuel Zapata//

import time

def get_recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * get_recursive_factorial(n-1)    


def get_iteractive_factorial(n):
    factorial_total = 1
    while n > 1:
        factorial_total *= n
        n -=1
    return factorial_total    


start_time=time.time()
get_recursive_factorial(10000)
print("recursion---%s seconds---"%(time.time()-start_time))
start_time=time.time()
get_iteractive_factorial(10000)
print("iteration---%sseconds---"%(time.time()-start_time))
