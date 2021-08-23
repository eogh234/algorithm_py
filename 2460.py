data = []

for _ in range(10):
    data.append((map(int, input().split())))

people = 0
answer = []

for off, on in data:
    people += on - off

    if on > off:
        answer.append(people)

print(max(answer))