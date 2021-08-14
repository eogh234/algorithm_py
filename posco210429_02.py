prices = [
    [10, 20, 30, 40, 50, 60, 70, 80],
    [20, 20, 20, 20, 20, 20, 20, 20]
]

multipleShopPrices = list(zip(*prices))

result = []

totalPrice = 0
for price in multipleShopPrices:
    totalPrice += min(price)

result.append(totalPrice)

totalPrice = sum(prices[0])
for price in prices:
    totalPrice = min(totalPrice, sum(price))
result.append(totalPrice)

print(result)