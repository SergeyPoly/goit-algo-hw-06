# Перетворення графа NetworkX у словникову структуру для роботи з алгоритмом
def convert_graph_to_dict(weighted_graph):
    graph_dict = {node: {} for node in weighted_graph.nodes()}
    for u, v, data in weighted_graph.edges(data=True):
        graph_dict[u][v] = data['weight']
        graph_dict[v][u] = data['weight']
    return graph_dict


# Відтворення найкоротшого шляху від початкової вершини до цільової.
def get_shortest_path(previous_vertices, start, target):
    path = []
    current_vertex = target
    while current_vertex is not None:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]
    return path if path[0] == start else None


