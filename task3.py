import networkx as nx
import matplotlib.pyplot as plt
from data import cities, roads_with_length

# Створюємо граф
weighted_graph = nx.Graph()

# Додавання вершин (обласні центри України)
weighted_graph.add_nodes_from(cities)

# Додавання ребер з вагами (ваги - умовні відстані між містами у км)
weighted_graph.add_weighted_edges_from(roads_with_length)

# Знаходження шляху між двома конкретними містами
source_city = "Львів"
target_city = "Харків"

shortest_path = nx.single_source_dijkstra_path(weighted_graph, source_city)[target_city]
shortest_length = nx.single_source_dijkstra_path_length(weighted_graph, source_city)[target_city]

print(f"\nНайкоротший шлях між {source_city} і {target_city}: {shortest_path}, Довжина: {shortest_length} км")