from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited = [False] * n

def dfs(graph, v, visited):
    visited[v] = True
    print(v+1, end=' ')
    graph[v].sort()
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v+1, end=' ')
        graph[v].sort()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, v-1, visited)
visited = [False] * n
print()
bfs(graph, v-1, visited)