n = int(input())

data = list(map(int, input().split()))
di = [1] * n
dd = [1] * n

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            di[i] = max(di[j] + 1, di[i])
        if data[n - i] > data[n - j - 1]:
            dd[n - i] = max(dd[n - j - 1] + 1, dd[n - i])

d = []
for i in range(n):
    d.append(di[i] + dd[i])

print(max(d) - 1)