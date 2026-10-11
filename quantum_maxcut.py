import networkx as nx
import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from scipy.optimize import minimize

# Opti-Q: Weighted Max-Cut Graph
G = nx.Graph()

G.add_weighted_edges_from([
    (0, 1, 3),
    (0, 2, 2),
    (1, 2, 4),
    (1, 3, 5),
    (2, 3, 1)
])

n = G.number_of_nodes()
edges = list(G.edges(data="weight"))

def create_qaoa_circuit(gamma, beta):
    qc = QuantumCircuit(n)

    # Initial superposition
    qc.h(range(n))

    # Cost layer
    for u, v, weight in edges:
        qc.rzz(2 * gamma * weight, u, v)

    # Mixer layer
    for q in range(n):
        qc.rx(2 * beta, q)

    return qc

def cut_weight(bitstring):
    bits = [int(b) for b in bitstring[::-1]]

    return sum(
        weight
        for u, v, weight in edges
        if bits[u] != bits[v]
    )

def objective(params):
    gamma, beta = params

    qc = create_qaoa_circuit(gamma, beta)
    qc.measure_all()

    simulator = AerSimulator()
    counts = simulator.run(
        qc,
        shots=1024
    ).result().get_counts()

    total = sum(counts.values())

    average_cut = sum(
        cut_weight(bits) * count
        for bits, count in counts.items()
    ) / total

    return -average_cut

# Optimize QAOA parameters
result = minimize(
    objective,
    x0=[0.5, 0.5],
    method="COBYLA",
    options={"maxiter": 40}
)

# Final measurement
gamma, beta = result.x

qc = create_qaoa_circuit(gamma, beta)
qc.measure_all()

simulator = AerSimulator()
counts = simulator.run(
    qc,
    shots=4096
).result().get_counts()

print("\n--- Opti-Q: QAOA Max-Cut Results ---")
print("Optimized gamma:", gamma)
print("Optimized beta:", beta)

print("\nMeasured bitstrings and cut weights:")

for bits, count in sorted(
    counts.items(),
    key=lambda item: cut_weight(item[0]),
    reverse=True
):
    print(
        "Bitstring:", bits,
        "| Cut weight:", cut_weight(bits),
        "| Counts:", count
    )

best_bits = max(counts, key=lambda b: cut_weight(b))

print("\nBest measured bitstring:", best_bits)
print("Best measured cut weight:", cut_weight(best_bits))
print("Classical optimum for this graph: 12")
import csv
import os

os.makedirs("results", exist_ok=True)

with open("results/qaoa_measurements.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Bitstring", "Cut Weight", "Count"])

    for bits, count in counts.items():
        writer.writerow([bits, cut_weight(bits), count])

print("Results saved to results/qaoa_measurements.csv")