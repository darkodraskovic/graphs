import graph, data


def test_dfs_count():
    g = data.g_connected
    count = graph.dfs(g)
    assert count == 1

    g = data.g_disconnected
    count = graph.dfs(g)
    assert count == 3


def test_bfs_connected():
    assert graph.bfs(data.g_connected, 0, 9) == [0, 2, 3, 1, 9]
    assert graph.bfs(data.g_connected, 9, 0) == [9, 1, 3, 2, 0]
    assert graph.bfs(data.g_connected, 6, 11) == [6, 3, 4, 5, 11]
    assert graph.bfs(data.g_connected, 11, 6) == [11, 5, 4, 3, 6]
