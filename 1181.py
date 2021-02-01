import sys

n = int(sys.stdin.readline().rstrip())

data = set()

for i in range(n):
    data.add(sys.stdin.readline().rstrip())

data = list(data)
data.sort(key=lambda str : (len(str), str))

for str in data:
    print(str)