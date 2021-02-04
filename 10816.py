import sys


def upper_bound(array, target, start, end):
    while start < end:
        mid = (start + end) // 2

        if array[mid] > target:
            end = mid
        else:
            start = mid + 1
    return end + 1


def lower_bound(array, target, start, end):
    while start < end:
        mid = (start + end) // 2

        if array[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return end + 1


n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())

exist = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()

for i in range(m):
    print(upper_bound(data, exist[i], 0, n) - lower_bound(data, exist[i], 0, n), end=' ')
