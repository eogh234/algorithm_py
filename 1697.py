from collections import deque

n, k = map(int, input().split())

visited = [0] * 100001
dx = [1, -1, 2]

def bfs(cur, target):
    queue = deque()
    queue.append(cur)
    visited[cur] = 0

    while queue:
        x = queue.popleft()
        if x == target:
            print(visited[x])
            return 0
        for i in range(3):
            if i == 2:
                nx = x * dx[i]
            else:
                nx = x + dx[i]
            if nx < 0 or nx > 100000:
                continue
            if visited[nx] > 0:
                continue
            visited[nx] = visited[x] + 1
            if nx == target:
                print(visited[nx])
                return 0
            queue.append(nx)


bfs(n, k)
