import graph, data


def test_dfs_count():
    g = data.g_connected
    count = graph.dfs(g)
    assert count == 1

    g = data.g_disconnected
    count = graph.dfs(g)
    assert count == 3
