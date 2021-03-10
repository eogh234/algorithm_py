import sys


n = int(sys.stdin.readline().rstrip())
d = [0] * (n + 1)
d[1] = 1
if n > 1:
    d[2] = 2

if n != 1 or n != 2:
    for i in range(3, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 15746

print(d[n])