import networkx as nx

G = nx.DiGraph()

G.add_edge("A", "B", weight=3)
G.add_edge("A", "C", weight=2)
G.add_edge("B", "C", weight=1)
G.add_edge("B", "D", weight=4)
G.add_edge("C", "D", weight=5)
G.add_edge("E", "D", weight=2)

shortest_path = nx.shortest_path(G, source="A", target="D", weight="weight")

print("Shortest Path:", shortest_path)
total_weight = sum(G[u][v]['weight'] for u, v in zip(shortest_path, shortest_path[1:]))
print("Total Weight:", total_weight)
