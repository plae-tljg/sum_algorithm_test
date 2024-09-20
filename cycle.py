from typing import List
import numpy as np

def find_cycles(node_names: List[str], weights: List[List[int]]) -> None:
    num_nodes = len(node_names)
    visited = set()
    current_path = []
    cycles = []

    weights = np.array(weights)

    def dfs(node: int) -> None:
        visited.add(node)
        current_path.append(node)

        for neighbor in range(num_nodes):
            if neighbor != node:
                if neighbor not in visited:
                    dfs(neighbor)
                elif neighbor in current_path:
                    # Cycle found
                    cycle = [node_names[i] for i in current_path[current_path.index(neighbor):]]
                    cycle_path = current_path[current_path.index(neighbor):]
                    cycle_weight = sum(weights[cycle_path[i]][cycle_path[i+1]] for i in range(len(cycle_path)-1))
                    cycle_weight += weights[cycle_path[-1]][cycle_path[0]]
                    if cycle_weight > 0:
                        cycles.append(cycle)

        current_path.pop()
        visited.remove(node)

    for node in range(num_nodes):
        dfs(node)

    for i, cycle in enumerate(cycles):
        print(f"Cycle {i+1}: {cycle}")
        cycle_path = [node_names.index(node) for node in cycle]
        cycle_weight = sum(weights[cycle_path[i]][cycle_path[i+1]] for i in range(len(cycle_path)-1))
        cycle_weight += weights[cycle_path[-1]][cycle_path[0]]
        print(f"Sum of weights: {cycle_weight}")
        print()


# Example usage
node_names = ['A', 'B', 'C', 'D']
weights = [
    [0, 1, 2, 3],
    [4, 0, 5, 6],
    [7, 8, 0, 9],
    [10, 11, 12, 0]
]

find_cycles(node_names, weights)