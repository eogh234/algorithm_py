from collections import deque
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = []
queue = deque()

for i in range(m):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(y, x):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[ny][nx] == -1:
            continue
        if graph[ny][nx] == 0:
            queue.append([ny, nx])
            graph[ny][nx] = graph[y][x] + 1


result = 0

for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append([i, j])

while queue:
    y, x = queue.popleft()
    bfs(y, x)

result = max(map(max, graph)) - 1

for i in range(m):
    if graph[i].count(0) > 0:
        result = -1
        break

print(result)
