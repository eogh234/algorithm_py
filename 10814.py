import sys

n = int(sys.stdin.readline().rstrip())

data = []
for i in range(n):
    age, name = sys.stdin.readline().rstrip().split()
    data.append((int(age), name, i))

data.sort(key=lambda person: (person[0], person[2]))

for person in data:
    print(person[0], person[1])