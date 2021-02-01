import sys
n = int(sys.stdin.readline().rstrip())

data = []
for _ in range(n):
    data.append(int(sys.stdin.readline().rstrip()))
data.sort()

for i in range(n):
    print(data[i])