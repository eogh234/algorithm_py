import sys

k, n = map(int, sys.stdin.readline().rstrip().split(' '))
data = list()

for i in range(k):
    data.append(int(sys.stdin.readline().rstrip()))

start = 0
end = max(data)

result = 0
while start <= end:
    count = 0
    mid = (start + end) // 2
    if mid == 0:
        result = end
        break
    for l in data:
        count += l // mid
    if count < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)