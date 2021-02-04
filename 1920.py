import sys


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            print(1)
            return True
        elif array[mid] < target:
            start = mid + 1
        elif array[mid] > target:
            end = mid - 1
        else:
            return None
    print(0)
    return False


n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())

exist = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()

for i in exist:
    binary_search(data, i, 0, n - 1)

