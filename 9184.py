import sys

d = [[[0] * 51 for _ in range(51)] for _ in range(51)]


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if d[a][b][c] != 0:
        return d[a][b][c]
    elif a > 20 or b > 20 or c > 20:
        d[a][b][c] = w(20, 20, 20)
        return d[a][b][c]
    elif a < b < c:
        d[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return d[a][b][c]
    else:
        d[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return d[a][b][c]


while True:
    a, b, c = map(int, sys.stdin.readline().rstrip().split())

    if a == -1 and b == -1 and c == -1:
        break

    print('w({0}, {1}, {2}) ='.format(a, b, c), w(a, b, c))
