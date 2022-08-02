import time
import sys

# def factorial(n):
#     result = 1

#     for i in range(1, n+1):
#         result *= i

#     return result

def loop_factorial(n):

    result = 1

    while n > 1:
        result *= n
        n -= 1

    return result


def recursion_factorial(n):

    if n == 1:
        return 1

    return n * recursion_factorial(n-1)


def run():
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(1000000)
    print(sys.getrecursionlimit())

    n = 50000

    starts = time.time()
    loop_factorial(n)
    ends = time.time()
    print(ends - starts)

    starts = time.time()
    recursion_factorial(n)
    ends = time.time()
    print(ends - starts)


if __name__ == '__main__':
    run()

# 100

# 4.506111145019531e-05
# 0.0001068115234375

# 1000

# 0.0008966922760009766
# 0.002058744430541992

# 10000

# 0.055904388427734375
# 0.042594194412231445

# 50000

# 100000

# 200000

# 350000

# 500000
