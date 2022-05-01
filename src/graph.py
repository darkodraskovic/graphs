from collections import deque


def _dfs_visit(node: int, graph: list[list[int]], visited: list[bool]):
    if visited[node]:
        return
    print(node, end=", ")
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
            print()
    print(f"count: {count}")
    return count


def _bfs_visit(
    node: int,
    graph: list[list[int]],
    enqueued: list[bool],
    parents: list[int | None],
    queue: deque,
):
    for neighbor in graph[node]:
        if enqueued[neighbor]:
            continue
        queue.append(neighbor)
        parents[neighbor] = node
        enqueued[neighbor] = True


def _bfs_compute_path():
    ...


def bfs(graph: list[list[int]], start_node: int = 0):
    enqueued: list[bool] = [False] * len(graph)
    parents: list[int | None] = [None] * len(graph)
    queue: deque = deque()

    queue.append(start_node)
    enqueued[start_node] = True
    while len(queue) > 0:
        node = queue.popleft()
        _bfs_visit(node, graph, enqueued, parents, queue)
