n = int(input())

time = list(map(int, input().split()))

result = 0

time.sort()

for i in range(n):
    for j in range(i + 1):
        result += time[j]

print(result)