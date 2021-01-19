n = int(input())
time = list()
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    time.append(data)

time.sort(key=lambda x: [x[1], x[0]])

curEnd = -1
for i in range(n):
    if time[i][0] == time[i][1]:
        result += 1
        curEnd = time[i][1]
    elif curEnd <= time[i][0]:
        result += 1
        curEnd = time[i][1]

print(result)
