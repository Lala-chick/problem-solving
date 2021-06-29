import sys
import heapq

def dijkstra(graph, start, num_nodes):
    queue = []
    heapq.heappush(queue, (0, start))
    distance = [1e10] * (num_nodes + 1)
    distance[start] = 0

    while queue:
        dist, cur_node = heapq.heappop(queue)

        if distance[cur_node] < dist:
            continue

        for next_dist, next_node in graph[cur_node]:
            next_dist += dist
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heapq.heappush(queue, (next_dist, next_node))
    
    return distance


V, E = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())
map_ = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = list(map(int, sys.stdin.readline().split()))
    map_[u].append((w,v))

distances = dijkstra(map_, K, V)

for dist in distances[1:]:
    print("INF" if dist == 1e10 else dist)