import networkx as nx
import itertools
import numpy as np
import matplotlib.pyplot as plt

def held_karp(tsp_matrix):
    n = len(tsp_matrix)
    dp = {}
    parent = {}

    for k in range(1, n):
        dp[(1 << k, k)] = tsp_matrix[0][k]
        parent[(1 << k, k)] = 0

    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            for k in subset:
                prev_bits = bits & ~(1 << k)
                min_dist = float('inf')
                min_prev = -1
                for m in subset:
                    if m == k:
                        continue
                    prev = dp.get((prev_bits, m), float('inf')) + tsp_matrix[m][k]
                    if prev < min_dist:
                        min_dist = prev
                        min_prev = m
                dp[(bits, k)] = min_dist
                parent[(bits, k)] = min_prev

    bits = (1 << n) - 2
    min_cost = float('inf')
    last = -1
    for k in range(1, n):
        cost = dp.get((bits, k), float('inf')) + tsp_matrix[k][0]
        if cost < min_cost:
            min_cost = cost
            last = k

    if min_cost == float('inf'):
        return False, None

    path = [0]
    bits = (1 << n) - 2
    while last != 0:
        path.append(last)
        prev = parent[(bits, last)]
        bits &= ~(1 << last)
        last = prev
    path.append(0)
    path = path[::-1]
    return True, path

def format_path(path, nodes):
    return " → ".join(nodes[i] for i in path)

def graph_to_tsp_matrix(graph):
    nodes = list(graph.nodes)
    node_index = {node: i for i, node in enumerate(nodes)}
    n = len(nodes)
    tsp_matrix = np.full((n, n), float('inf'))

    for u, v, data in graph.edges(data=True):
        i, j = node_index[u], node_index[v]
        weight = data.get('weight', 1)
        tsp_matrix[i][j] = weight
        tsp_matrix[j][i] = weight

    return tsp_matrix, nodes

def draw_graph(graph, graph_id):
    plt.figure(figsize=(6, 6))
    plt.title(f"Grafo {graph_id}")
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray', font_weight='bold')
    plt.savefig(f"HeldKarp/grafo_{graph_id}.png")
    plt.close()

def process_graph(edges, graph_id):
    G = nx.Graph()
    G.add_edges_from(edges)

    print(f"\n--- Grafo {graph_id} ---")
    tsp_matrix, nodes = graph_to_tsp_matrix(G)
    is_ham, path = held_karp(tsp_matrix)

    print("É Hamiltoniano?", is_ham)
    if is_ham:
        print("Ciclo Hamiltoniano:", [nodes[i] for i in path])
        print("Caminho formatado:", format_path(path, nodes))

    print("\nMatriz TSP:")
    print("   ", "  ".join(nodes))
    for i, row in enumerate(tsp_matrix):
        row_str = "  ".join(f"{val if val != float('inf') else '-':>3}" for val in row)
        print(f"{nodes[i]}  {row_str}")

    draw_graph(G, graph_id)

def main():
    grafos = [
        [('A','B'), ('B','C'), ('C','D'), ('D','A')],
        [('A','B'), ('B','C'), ('C','D')],
        [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'E')],
        [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'A')],
        [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E')],
        [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'A')],
        [('A', 'B'), ('B', 'C'), ('C', 'E'), ('E', 'D')],
        [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A'), ('A', 'C')],
        [('A', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'D'), ('D', 'E')],
        [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'A'), ('B', 'E'), ('C', 'F')]
    ]

    for i, edges in enumerate(grafos, 1):
        process_graph(edges, i)

if __name__ == "__main__":
    main()
