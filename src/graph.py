from collections import deque

# Depth-first search


def _dfs_visit(node: int, graph: list[list[int]], visited: list[bool]):
    if visited[node]:
        return
    visited[node] = True
    for neighbor in graph[node]:
        _dfs_visit(neighbor, graph, visited)


def dfs(graph: list[list[int]]) -> int:
    count: int = 0
    visited: list[bool] = [False] * len(graph)
    for i in range(len(graph)):
        if not visited[i]:
            count += 1
            _dfs_visit(i, graph, visited)
    return count


# Breadth-first search


def _bfs_solve_path(
    graph: list[list[int]], start_node: int = 0, end_node: int = 0
) -> list[int | None]:
    enqueued: list[bool] = [False] * len(graph)
    parents: list[int | None] = [None] * len(graph)
    queue: deque = deque()

    queue.append(start_node)
    enqueued[start_node] = True
    while len(queue) > 0:
        node = queue.popleft()
        if node == end_node:
            break
        for neighbor in graph[node]:
            if enqueued[neighbor]:
                continue
            queue.append(neighbor)
            parents[neighbor] = node
            enqueued[neighbor] = True

    return parents


def _bfs_reconstruct_path(parents: list[int | None], end_node: int) -> list[int | None]:
    path: list[int | None] = []

    current: int | None = end_node
    while current is not None:
        path.append(current)
        current = parents[current]
    path.reverse()
    return path


def bfs(
    graph: list[list[int]], start_node: int = 0, end_node: int = 0
) -> list[int | None]:
    parents = _bfs_solve_path(graph, start_node, end_node)
    return _bfs_reconstruct_path(parents, end_node)
