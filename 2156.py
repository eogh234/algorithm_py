n = int(input())

data = [0] * (n + 1)
for i in range(n):
    data[i + 1] = int(input())

d = [0] * (n + 1)

d[1] = data[1]
if n > 1:
    d[2] = data[1] + data[2]

if n > 2:
    for i in range(3, n + 1):
        d[i] = max(d[i - 2] + data[i], d[i - 3] + data[i - 1] + data[i])
        d[i] = max(d[i - 1], d[i])

print(d[n])