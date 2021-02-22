import sys

n, c = map(int, sys.stdin.readline().rstrip().split())
data = list()
for i in range(n):
    data.append(int(sys.stdin.readline().rstrip()))

data.sort()

start = 1
end = data[-1] - data[0]


def possible(current, wifi):
    i = current + 1
    while i < n:
        if wifi == 0:
            return True
        if data[i] - data[current] >= mid:
            wifi -= 1
            current = i
            i = current + 1
        else:
            i += 1
    if wifi == 0:
        return True
    return False


while start + 1 < end:
    mid = (start + end) // 2
    if possible(0, c - 1):
        start = mid
    else:
        end = mid

print(start)
