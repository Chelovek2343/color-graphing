# 🧠 Sudoku Solver using Graph Coloring

This project solves a standard 9×9 **Sudoku puzzle** using a **graph coloring approach** and visualizes the solution as a **graph**. Each cell is modeled as a vertex, and constraints are represented by graph edges. It showcases how classical constraint satisfaction problems can be approached using **graph theory**.

---

## 📚 How It Works

- Each cell in the Sudoku board is treated as a **graph vertex**.
- Edges are created between cells in the same **row**, **column**, or **3×3 box**.
- The solver uses **backtracking** to assign digits (colors) from 1 to 9 while obeying Sudoku rules (no adjacent nodes share the same digit).
- The final solution is visualized using `networkx` and `matplotlib`.

---

## 🛠 Requirements

- Python 3.7+
- `networkx`
- `matplotlib`

Install them using pip:

```bash
pip install networkx matplotlib
