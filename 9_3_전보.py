import sys
import heapq

INF = int(1e9)

n, m, c = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    x, y, z = map(int, sys.stdin.readline().split())

    graph[x].append((y, z))

def dijkstra(start):
    q = []

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        d, now = heapq.heappop(q)

        if distance[now] < d:
            continue
        for i in graph[now]:
            cost = d + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

city_count = 0
max_distance = 0

for d in distance:
    if d != INF:
        city_count += 1
        max_distance = max(max_distance, d)
print(city_count - 1, max_distance)