n = int(input())

data = list(map(int, input().split()))
d = [1] * n

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            d[i] = max(d[j] + 1, d[i])

print(max(d))