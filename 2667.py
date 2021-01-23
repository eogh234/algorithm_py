from collections import deque

n = int(input())

graph = list()

for i in range(n):
    graph.append(list(map(int, input())))

result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    graph[x][y] = 0
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                count += 1
                graph[nx][ny] = 0
                queue.append([nx, ny])
    return count


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = 0
            cnt = bfs(i, j)
            result.append(cnt)

print(len(result))
result.sort()
for i in result:
    print(i)