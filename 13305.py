n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

result = 0
curCity = 0
diffCity = 1

while diffCity < n:
    if price[diffCity] < price[curCity] and diffCity != n - 1:
        result += (distance[diffCity - 1] * price[curCity])
        curCity = diffCity
        diffCity += 1
    else:
        result += (distance[diffCity - 1] * price[curCity])
        diffCity += 1

print(result)