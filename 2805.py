import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
data = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(data)

data.sort(reverse=True)
result = 0
while start <= end:
    count = 0
    mid = (start + end) // 2
    for l in data:
        if l <= mid:
            break
        else:
            count += l - mid

    if count < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)