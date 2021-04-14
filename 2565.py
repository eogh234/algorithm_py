n = int(input())

data = []
d = [1] * n

for i in range(n):
    data.append(list(map(int, input().split())))

data.sort()

for i in range(n):
    for j in range(i):
        if data[i][1] > data[j][1]:
            d[i] = max(d[j] + 1, d[i])

print(len(data) - max(d))