n = int(input())

data = []
d = [0] * n

for _ in range(n):
    data.append(int(input()))

d[0] = data[0]
if n > 1:
    d[1] = d[0] + data[1]
if n > 2:
    d[2] = max(data[0] + data[2], data[1] + data[2])

if n > 3:
    for i in range(3, n):
        d[i] = max(d[i - 3] + data[i - 1] + data[i], d[i - 2] + data[i])

print(d[n - 1])