import sys

n = int(sys.stdin.readline().rstrip())

data = []

for i in range(n):
    data.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

data.sort(key=lambda e : (e[0], e[1]))

for i in range(n):
    for j in range(2):
        if j == 0:
            print(data[i][j], end=' ')
        else:
            print(data[i][j])