import sys

n = sys.stdin.readline().rstrip()

data = []
for ch in n:
    data.append(ch)

data.sort(reverse=True)

for i in data:
    print(i, end='')
