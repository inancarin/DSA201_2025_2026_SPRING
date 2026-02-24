import Factorial as f
import time
import math

if __name__ == "__main__":
    start = time.time() # return currect unix (epoch) time
    for i in range(1000000):
        res = f.factorial_recursive(100)
    end = time.time()
    elapsed = end - start
    print(elapsed, "seconds (recursive)")

    start = time.time() # return currect unix (epoch) time
    for i in range(1000000):
        res = f.factorial_nonrecursive(100)
    end = time.time()
    elapsed = end - start
    print(elapsed, "seconds (non recursive)")

    start = time.time() # return currect unix (epoch) time
    for i in range(1000000):
        res = math.factorial(100)
    end = time.time()
    elapsed = end - start
    print(elapsed, "seconds (math)")