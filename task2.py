import networkx as nx
import matplotlib.pyplot as plt
from data import cities, roads
from graph_search_algorithms import dfs_recursive, bfs_iterative

# Створюємо граф
road_graph = nx.Graph()

# Додавання вершин (обласні центри України)
road_graph.add_nodes_from(cities)

# Додавання ребер (основні автомагістралі між містами)
road_graph.add_edges_from(roads)

# Перетворення графа NetworkX у список суміжності
adjacency_list = {node: list(road_graph.neighbors(node)) for node in road_graph.nodes()}

# Тестування
print("DFS (рекурсивний):")
dfs_recursive(adjacency_list, "Київ")

print("\n\nBFS (ітеративний):")
bfs_iterative(adjacency_list, "Київ")