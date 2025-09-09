def has_cycle(V, edges):
    # Build adjacency list
    graph = {i: [] for i in range(V)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False

    # Run DFS for all components
    for i in range(V):
        if i not in visited:
            if dfs(i, -1):
                return True
    return False


# 🔹 Test Cases
print(has_cycle(5, [[0,1],[1,2],[2,3],[3,4],[4,0]]))  # True
print(has_cycle(3, [[0,1],[1,2]]))                    # False
print(has_cycle(4, [[0,1],[1,2],[2,0]]))              # True
print(has_cycle(5, []))                               # False (no edges)
print(has_cycle(2, [[0,1],[0,1]]))                    # True (parallel edges)
