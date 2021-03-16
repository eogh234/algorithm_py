n = int(input())

data = []

for i in range(n):
    data.append(list(map(int, input().split())))

d = []
for i in range(1, n + 1):
    d.append([0] * i)

d[0][0] = data[0][0]

for i in range(1, n):
    for j in range(i):
        if d[i][j] != 0:
            d[i][j] = max(d[i - 1][j - 1] + data[i][j], d[i - 1][j] + data[i][j])
        else:
            d[i][j] = d[i - 1][j] + data[i][j]
        d[i][j + 1] = d[i - 1][j] + data[i][j + 1]
print(max(d[n - 1]))