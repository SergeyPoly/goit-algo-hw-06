import networkx as nx
import matplotlib.pyplot as plt
from data import cities, roads

# Створюємо граф
road_graph = nx.Graph()

# Додавання вершин (обласні центри України)
road_graph.add_nodes_from(cities)

# Додавання ребер (основні автомагістралі між містами)
road_graph.add_edges_from(roads)

# Візуалізація графа
plt.figure(figsize=(12, 8))
nx.draw(
    road_graph, 
    with_labels=True, 
    node_color="skyblue", 
    node_size=500, 
    edge_color="gray", 
    font_size=8, 
    font_weight="bold"
)
plt.title("Транспортна мережа між обласними центрами України")
plt.show()

# Аналіз характеристик графа
print("Кількість вершин:", road_graph.number_of_nodes())
print("Кількість ребер:", road_graph.number_of_edges())
print("Середній ступінь вершин:", sum(dict(road_graph.degree()).values()) / road_graph.number_of_nodes())
print("\nСтупені вершин:")
for city, degree in road_graph.degree():
    print(f"{city}: {degree}")

