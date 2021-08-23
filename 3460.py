t = int(input())

for _ in range(t):
    n = int(input())
    pos = 0
    while n >= 1:
        if n % 2 == 1:
            if n == 1:
                print(pos)
            else:
                print(pos, end=' ')
        pos += 1
        n //= 2