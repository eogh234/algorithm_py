n, k = map(int, input().split())

data = list()
count = 0

for i in range(n):
    data.append(int(input()))

while k > 0:
    for num in reversed(data):
        if num > k:
            continue
        else:
            count += int(k / num)
            k -= (num * int(k / num))

print(count)