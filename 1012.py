from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(y, x, count):
    queue = deque()
    queue.append([y, x])
    graph[y][x] = 0

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[ny][nx] == 0:
                continue
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append([ny, nx])
    return count + 1

t = int(input())

for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                cnt = bfs(i, j, cnt)
    print(cnt)
