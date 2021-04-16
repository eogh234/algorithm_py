n = int(input())

data = list(map(int, input().split()))

d = [0] * n
d[0] = data[0]

for i in range(1, n):
    d[i] = max(d[i - 1] + data[i], data[i])

print(max(d))