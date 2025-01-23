import networkx as nx
import matplotlib.pyplot as plt
from data import cities, roads_with_length
from helpers import convert_graph_to_dict, get_shortest_path
from graph_search_algorithms import dijkstra

# Створюємо граф
weighted_graph = nx.Graph()

# Додавання вершин (обласні центри України)
weighted_graph.add_nodes_from(cities)

# Додавання ребер з вагами (ваги - умовні відстані між містами у км)
weighted_graph.add_weighted_edges_from(roads_with_length)

# Конвертація графа NetworkX у словникову структуру
graph_dict = convert_graph_to_dict(weighted_graph)

# Знаходження шляху між двома конкретними містами
source_city = "Львів"
target_city = "Харків"

distances, previous_vertices = dijkstra(graph_dict, source_city)
shortest_path = get_shortest_path(previous_vertices, source_city, target_city)
shortest_length = distances[target_city]

print(f"\nНайкоротший шлях між {source_city} і {target_city}: {shortest_path}, Довжина: {shortest_length} км")