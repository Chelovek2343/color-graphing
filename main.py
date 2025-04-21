import networkx as nx
import matplotlib.pyplot as plt

def build_sudoku_graph():
    G = nx.Graph()
    for row in range(9):
        for col in range(9):
            node = (row, col)
            G.add_node(node)
            for k in range(9):
                if k != col:
                    G.add_edge(node, (row, k))
                if k != row:
                    G.add_edge(node, (k, col))
            box_row, box_col = row // 3, col // 3
            for i in range(box_row * 3, box_row * 3 + 3):
                for j in range(box_col * 3, box_col * 3 + 3):
                    if (i, j) != node:
                        G.add_edge(node, (i, j))
    return G

def solve_sudoku_graph(board):
    G = build_sudoku_graph()

    def is_valid(node, value, assignment):
        for neighbor in G.neighbors(node):
            if assignment.get(neighbor) == value:
                return False
        return True

    def backtrack(assignment):
        if len(assignment) == 81:
            return assignment
        for row in range(9):
            for col in range(9):
                node = (row, col)
                if node not in assignment:
                    for value in range(1, 10):
                        if board[row][col] != 0:
                            assignment[node] = board[row][col]
                            return backtrack(assignment)
                        elif is_valid(node, value, assignment):
                            assignment[node] = value
                            result = backtrack(assignment)
                            if result:
                                return result
                            del assignment[node]
                    return None
        return None

    assignment = {(r, c): board[r][c]
                  for r in range(9) for c in range(9) if board[r][c] != 0}
    solution = backtrack(assignment)
    return solution

def draw_sudoku_graph(solution):
    G = build_sudoku_graph()
    pos = {(r, c): (c, -r) for r in range(9) for c in range(9)}  # grid layout

    labels = {node: solution[node] for node in G.nodes()}
    color_map = [solution[node] / 9 for node in G.nodes()]  # scale to [0,1] for colormap

    plt.figure(figsize=(8, 8))
    nx.draw(
        G,
        pos=pos,
        node_color=color_map,
        node_size=600,
        cmap=plt.cm.viridis,
        with_labels=True,
        labels=labels,
        font_color='white',
        font_size=10,
        width=0.2
    )
    plt.title("Sudoku Solved as Graph Coloring", fontsize=16)
    plt.axis('off')
    plt.show()

# Sudoku board
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

solution = solve_sudoku_graph(sudoku_board)

if solution:
    print("Sudoku solved — rendering graph...")
    draw_sudoku_graph(solution)
else:
    print("No solution found.")
