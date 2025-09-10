from collections import deque, defaultdict

def shortest_path_unweighted(V, edges, start, end):
    # Step 1: Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  
    visited = [False] * V
    distance = [-1] * V
    queue = deque([start])

    visited[start] = True
    distance[start] = 0
    while queue:
        node = queue.popleft()
        if node == end:
            return distance[node]

        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)

    return -1
