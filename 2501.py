n, k = map(int, input().split())
data = set()
for i in range(1, n + 1):
    if n % i == 0:
        data.add(i)
data = list(data)
data.sort()
answer = 0
if len(data) >= k:
    answer = data[k - 1]

print(answer)