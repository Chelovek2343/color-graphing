import networkx as nx
import matplotlib.pyplot as plt

def greedy_coloring(graph):
    result = {}
    for node in graph.nodes():
        neighbor_colors = {result[neighbor] for neighbor in graph.neighbors(node) if neighbor in result}
        color = 0
        while color in neighbor_colors:
            color += 1
        result[node] = color
    return result

# Пример графа
G = nx.Graph()
edges = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
G.add_edges_from(edges)

# Раскраска
coloring = greedy_coloring(G)

# Цветовая палитра
color_map = ['red', 'green', 'blue', 'orange', 'purple', 'cyan']

# Генерация цветов для узлов
node_colors = [color_map[coloring[node]] for node in G.nodes()]

# Отображаем граф
pos = nx.spring_layout(G)
plt.figure(figsize=(6, 4))
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1000)
plt.title("Graph Coloring (Greedy Algorithm)")
plt.show()
