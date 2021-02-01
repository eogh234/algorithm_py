import sys

n = int(sys.stdin.readline().rstrip())

count = [0] * 10001
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    count[num] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)