from collections import deque
import sys

def bfs(cur):
    queue = deque()
    queue.append(cur)
    visited[cur - 1] = 1

    while queue:
        v = queue.popleft()

        for i in graph[v - 1]:
            if visited[i - 1] == 0:
                queue.append(i)
                visited[i - 1] = visited[v - 1] * -1
            if visited[i - 1] != 0:
                if visited[i - 1] == visited[v - 1]:
                    return False

    return True


k = int(input())

for _ in range(k):
    isGraph = True
    v, e = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(v)]
    visited = [0] * v

    for i in range(e):
        v1, v2 = map(int, sys.stdin.readline().rstrip().split())
        if v1 != v2:
            graph[v1 - 1].append(v2)
            graph[v2 - 1].append(v1)

    for i in range(1, v + 1):
        if visited[i - 1] == 0:
            isGraph = bfs(i)
            if not isGraph:
                break
    if isGraph:
        print("YES")
    else:
        print("NO")
