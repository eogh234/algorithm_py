import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))

arr = [0]


def binary_search(start, end, target):
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid
        else:
            end = start = mid
    return end


for num in data:
    if num > arr[-1]:
        arr.append(num)
    else:
        start = 1
        end = len(arr) - 1
        idx = binary_search(start, end, num)
        arr[idx] = num

print(len(arr) - 1)
