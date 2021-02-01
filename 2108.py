import sys
import math

n = int(sys.stdin.readline().rstrip())
data = []
count = [0] * 8001
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    data.append(num)
    count[num + 4000] += 1

sum = 0
avg = 0
for i in data:
    sum += i
avg = round(sum / n)

print(avg)

data.sort()

center = math.floor(n / 2)
print(data[center])

max = max(count)
freq = []
for i in range(len(count)):
    if count[i] == max:
        freq.append(i)

if len(freq) > 1:
    mostFreq = freq[1]
else:
    mostFreq = freq[0]

print(mostFreq - 4000)

print(data[-1] - data[0])
