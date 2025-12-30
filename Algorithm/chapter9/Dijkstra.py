import math
import heapq

def dijkstra(graph, start):
    """Compute shortest-path distances and parents from start to all nodes."""
    distances = {node: math.inf for node in graph}
    distances[start] = 0

    parents = {node: None for node in graph}  # track the tree for path reconstruction
    pq = [(0, start)]  # (distance, node)

    while pq:
        current_distance, u = heapq.heappop(pq)

        # If this popped entry is stale, skip
        if current_distance > distances[u]:
            continue

        for v, w in graph[u].items():
            cand = current_distance + w
            if cand < distances[v]:
                distances[v] = cand
                parents[v] = u
                heapq.heappush(pq, (cand, v))

    return distances, parents

def reconstruct_path(parents, target):
    """Reconstruct a path from the start to `target` using the parents map."""
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = parents[cur]
    path.reverse()
    return path

if __name__ == "__main__":
    # Example graph (adjacency dict with weights)
    graph = {
        'start': {'a': 6, 'b': 2},
        'a':     {'fin': 1},
        'b':     {'a': 3, 'fin': 5},
        'fin':   {}
    }

    distances, parents = dijkstra(graph, 'start')
    print("Shortest path costs from 'start':", distances)
    print("Parents in the shortest path tree:", parents)

    # Example: shortest path to 'fin'
    path_to_fin = reconstruct_path(parents, 'fin')
    print("Shortest path to 'fin':", path_to_fin)
