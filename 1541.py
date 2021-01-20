n = input()

result = 0
sum = 0
cnt = 0
isMinus = False

stack = list()

for ch in n:
    if '0' <= ch <= '9':
        stack.append(int(ch))
        cnt += 1
    elif ch == '+':
        for s in stack:
            sum += s * (10 ** (cnt - 1))
            cnt -= 1
        stack.clear()
    elif ch == '-':
        if isMinus:
            for s in stack:
                sum += s * (10 ** (cnt - 1))
                cnt -= 1
            result -= sum
        else:
            for s in stack:
                sum += s * (10 ** (cnt - 1))
                cnt -= 1
            result += sum
        sum = 0
        isMinus = True
        stack.clear()

for s in stack:
    sum += s * (10 ** (cnt - 1))
    cnt -= 1

if isMinus:
    result -= sum
else:
    result += sum

print(result)