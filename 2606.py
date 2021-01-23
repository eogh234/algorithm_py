n = int(input())
m = int(input())

graph = [[] for i in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

visited = [False] * n
result = 0

def dfs(v, result):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            result = dfs(i, result + 1)
    return result

print(dfs(0, 0))