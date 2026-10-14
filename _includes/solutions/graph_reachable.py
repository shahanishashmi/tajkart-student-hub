from collections import deque


def graph_reachable(graph, start, target):
    if start not in graph or target not in graph:
        return False
    pending = deque([start])
    visited = {start}
    while pending:
        node = pending.popleft()
        if node == target:
            return True
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                pending.append(neighbor)
    return False
