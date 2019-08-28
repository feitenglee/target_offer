# 2019-08-27
# by lifieteng@live.com
# 斐波那契数列/青蛙跳台阶
import sys

def fibonacci_recursion(n):
    if n < 0:
        print("n must be non-nagtive!")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def fibonacci_loop(n):
    if n < 0:
        print("n must be non-nagtive!")
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib0, fib1, fibn = 0, 1, 0
    for i in range(2,n+1):
        fibn = fib0 + fib1
        # fib0, fib1 = fib1, fibn
        fib0 = fib1
        fib1 = fibn
    return fibn

if __name__ == "__main__":
    n = int(sys.argv[1])
    res1 = fibonacci_recursion(n)
    res2 = fibonacci_loop(n)
    print("recursive:{}\tloop:{}".format(res1,res2))