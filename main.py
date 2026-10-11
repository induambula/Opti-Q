import networkx as nx
import matplotlib.pyplot as plt

# Create a weighted graph

G = nx.Graph()

# Add weighted edges

G.add_weighted_edges_from([
(0, 1, 3),
(0, 2, 2),
(1, 2, 4),
(1, 3, 5),
(2, 3, 1)
])

# Display graph information

print("Opti-Q: Max-Cut Optimization")
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())

# Draw the graph

pos = nx.spring_layout(G, seed=42)

nx.draw(
G,
pos,
with_labels=True,
node_size=1500,
font_size=12
)

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("Opti-Q: Weighted Graph for Max-Cut")
plt.savefig("results/weighted_graph.png", dpi=300, bbox_inches="tight")
plt.show()
from itertools import product

# Find the best Max-Cut
nodes = list(G.nodes())
best_cut = None
best_weight = -1

for bits in product([0, 1], repeat=len(nodes)):
    group_a = []
    group_b = []

    for node, bit in zip(nodes, bits):
        if bit == 0:
            group_a.append(node)
        else:
            group_b.append(node)

    cut_weight = sum(
        G[u][v]["weight"]
        for u, v in G.edges()
        if bits[nodes.index(u)] != bits[nodes.index(v)]
    )

    if cut_weight > best_weight:
        best_weight = cut_weight
        best_cut = (group_a, group_b)

print("\n--- Max-Cut Result ---")
print("Group A:", best_cut[0])
print("Group B:", best_cut[1])
print("Maximum cut weight:", best_weight)
from itertools import product

nodes = list(G.nodes())
best_weight = -1
best_cut = None

for bits in product([0, 1], repeat=len(nodes)):
    cut_weight = sum(
        G[u][v]["weight"]
        for u, v in G.edges()
        if bits[nodes.index(u)] != bits[nodes.index(v)]
    )

    if cut_weight > best_weight:
        best_weight = cut_weight
        best_cut = bits

print("\n--- Max-Cut Result ---")
print("Best partition:", best_cut)
print("Maximum cut weight:", best_weight)
