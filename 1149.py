n = int(input())
home = []
d = []

for i in range(n):
    home.append(list(map(int, input().split())))

d.append(home[0])

for i in range(1, n):
    d.append([0] * 3)
    d[i][0] = min(d[i - 1][1], d[i - 1][2]) + home[i][0]
    d[i][1] = min(d[i - 1][0], d[i - 1][2]) + home[i][1]
    d[i][2] = min(d[i - 1][0], d[i - 1][1]) + home[i][2]

print(min(d[n - 1]))