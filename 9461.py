def P(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    for i in range(4, n + 1):
        d[i] = d[i - 3] + d[i - 2]
    return d[n]


t = int(input())
d = [0] * 101
d[1] = 1
d[2] = 1
d[3] = 1
for _ in range(t):
    n = int(input())

    print(P(n))
