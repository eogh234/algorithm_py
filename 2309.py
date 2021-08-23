from itertools import combinations
data = []
for _ in range(9):
    data.append(int(input()))

answer = []

cases = list(combinations(data, 7))

for case in cases:
    if sum(case) == 100:
        answer = list(case)
        answer.sort()
        break

for num in answer:
    print(num)