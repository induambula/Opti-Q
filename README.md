# Opti-Q: Quantum-Assisted Max-Cut Optimization

## 1. Project Overview
Opti-Q explores the Max-Cut optimization problem using a classical algorithm and the Quantum Approximate Optimization Algorithm (QAOA).

The project uses a weighted graph with four nodes and five edges to compare the solutions produced by classical computation and a local quantum simulator.

## 2. Problem Statement
Max-Cut divides the nodes of a graph into two groups to maximize the total weight of edges connecting different groups.

Finding good solutions to optimization problems can be challenging as problem size increases.

## 3. Proposed Solution
Opti-Q implements:
- Classical Max-Cut optimization.
- QAOA using Qiskit.
- Local quantum circuit simulation using Qiskit Aer.
- Measurement result collection and comparison.

## 4. Technologies Used
- Python
- NetworkX
- Matplotlib
- Qiskit
- Qiskit Aer
- SciPy

## 5. Graph Details
- Number of nodes: 4
- Number of edges: 5
- Classical optimum cut weight: 12

## 6. Results
The local QAOA simulation produced a measured solution with a cut weight of 12 for the test graph.

The classical optimum for this graph is also 12.

This result demonstrates that the simulated QAOA circuit can produce an optimal solution for this small example. It does not establish quantum advantage.

## 7. Project Structure
- main.py: Classical Max-Cut implementation and graph visualization.
- quantum_maxcut.py: QAOA circuit, parameter optimization, and measurements.
- results/weighted_graph.png: Weighted graph visualization.
- results/qaoa_results.txt: QAOA experiment summary.
- results/qaoa_measurements.csv: Measurement data.
- results/benchmark_results.csv: Classical and simulator comparison.

## 8. Current Limitations
Experiments currently use a local simulator.

Testing on the challenge's specified quantum processors and completing the required processor benchmarks remain future tasks.

## 9. Future Scope
- Evaluate performance on larger graphs.
- Compare results across the required quantum processors.
- Analyze solution quality, execution time, and measurement statistics.
- Investigate the impact of noise on QAOA performance.

## 10. Conclusion
Opti-Q is an educational exploration of quantum optimization using QAOA for the weighted Max-Cut problem.