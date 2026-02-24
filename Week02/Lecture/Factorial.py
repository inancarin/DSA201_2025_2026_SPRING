def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)

def factorial_nonrecursive(n):
    res = 1
    for i in range(2, n+1):
        res = res * i
    return res

def countDown_nonRecursive(x):
    for i in range(x, 0, -1):
        print(i)

def countDown_recursive(x):
    if x > 0:
        print(x)
        countDown_recursive(x-1)

if __name__ == "__main__":
    res = factorial_recursive(4)
    print(res)

    res2 = factorial_nonrecursive(4)
    print(res2)

    #countDown_nonRecursive(10)
    countDown_recursive(10)