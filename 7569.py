from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for i in range(h)]
queue = deque()

for i in range(h):
    for j in range(n):
        graph[i].append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(x, y, z):
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
            continue
        if graph[nz][nx][ny] == -1:
            continue
        if graph[nz][nx][ny] == 0:
            queue.append([nx, ny, nz])
            graph[nz][nx][ny] = graph[z][x][y] + 1


result = 0

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                queue.append([i, j, k])

while queue:
    x, y, z = queue.popleft()
    bfs(x, y, z)

resultList = []
for i in range(h):
    resultList.append(max(map(max, graph[i])))

maxResult = resultList[0]
for result in resultList:
    if maxResult < result:
        maxResult = result
result = maxResult - 1
for j in range(h):
    for i in range(n):
        if graph[j][i].count(0) > 0:
            result = -1
            break

print(result)
