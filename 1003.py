import sys

t = int(sys.stdin.readline().rstrip())

d = [0] * 41

d[1] = 1
d[2] = 1


def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif d[x] != 0:
        return d[x]
    else:
        d[x] = fibo(x - 1) + fibo(x - 2)
        return d[x]


for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        print(1, 0)
    else:
        print(fibo(n - 1), fibo(n))