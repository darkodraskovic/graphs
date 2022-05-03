import graph, data

# graph.dfs(data.g_connected)
# graph.dfs(data.g_disconnected)

graph.bfs(data.g_connected, 0, 9)
graph.bfs(data.g_connected, 9, 0)
graph.bfs(data.g_connected, 6, 11)
graph.bfs(data.g_connected, 11, 6)
