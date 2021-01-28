from collections import deque

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]
visited = []

def bfs(curX, curY, tarX, tarY):
    queue = deque()
    queue.append([curX, curY])

    while queue:
        x, y = queue.popleft()
        if x == tarX and y == tarY:
            print(visited[x][y])
            return 0
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= l or ny >= l:
                continue
            if visited[nx][ny] == 0:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1


n = int(input())

for _ in range(n):
    l = int(input())
    visited = [[0] * l for _ in range(l)]

    curX, curY = map(int, input().split())
    tarX, tarY = map(int, input().split())

    bfs(curX, curY, tarX, tarY)