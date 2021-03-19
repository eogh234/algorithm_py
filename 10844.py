n = int(input())

d = []

for i in range(n + 1):
    d.append([0] * 11)

for i in range(1, 10):
    d[1][i] = 1

for i in range(2, n + 1):
    d[i][0] = d[i - 1][1]
    for j in range(1, 10):
        d[i][j] = (d[i - 1][j - 1] + d[i - 1][j + 1]) % 1000000000

result = 0

for i in range(0, 11):
    result += d[n][i]

print(result % 1000000000)
