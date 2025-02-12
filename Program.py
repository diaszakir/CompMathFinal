import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Task1, Task2, Task3

def execute_Task1(a, b, tol=1e-6):
    try:
        a, b = float(a), float(b)
        if a >= b:
            raise ValueError("The beginning must be smaller than the end!")
    except ValueError:
        messagebox.showerror("Error", "Type correct numbers")
        return None, None

    fig, true_root, absolute_error = Task1.run(a, b, tol)

    if true_root is None:
        messagebox.showerror("Error", "Invalid initial values. f(a) and f(b) must be of different signs.")
        return None, None

    return fig, f"True Root: {true_root:.6f}\nAbsolute Error: {absolute_error:e}"

def execute_Task2(a, b, tol=1e-6):
    try:
        a, b = float(a), float(b)
        if a >= b:
            raise ValueError("The beginning must be smaller than the end!")
    except ValueError:
        messagebox.showerror("Error", "Type correct numbers")
        return None

    try:
        root_newton, iter_newton, err_newton, root_false, iter_false, err_false = Task2.run(a, b, tol)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return None

    return (f"Newton-Raphson:\nRoot: {root_newton:.6f}, Iterations: {iter_newton}, Relative Error: {err_newton:e}\n"
            f"False-Position:\nRoot: {root_false:.6f}, Iterations: {iter_false}, Relative Error: {err_false:e}")

def execute_Task3(A_entries, b_entries):
    try:
        A = np.array([[float(A_entries[i][j].get()) for j in range(3)] for i in range(3)])
        b = np.array([float(b_entries[i].get()) for i in range(3)])
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
        return None

    x0 = np.zeros(len(b))
    root = Task3.run(A, b, x0, tol=1e-6, max_iter=100)
    
    return f"Root: {np.round(root, 6)}"

class NumericalMethodsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Numerical Methods GUI")
        self.root.geometry("900x700")

        self.method_label = ttk.Label(root, text="Select Method:")
        self.method_label.pack(pady=5)

        self.method_var = tk.StringVar()
        self.method_combobox = ttk.Combobox(root, textvariable=self.method_var, state="readonly")
        self.method_combobox["values"] = (
            "Graphical Method",
            "Root-Finding Comparison",
            "Jacobi Method",
        )
        self.method_combobox.pack()
        self.method_combobox.bind("<<ComboboxSelected>>", self.show_input_fields)

        self.input_frame = ttk.Frame(root)
        self.input_frame.pack(pady=10)

        self.canvas_frame = ttk.Frame(root)
        self.canvas_frame.pack(pady=20)

        self.run_button = ttk.Button(root, text="Run Method", command=self.run_method)
        self.run_button.pack()

        self.output_text = tk.Text(root, height=5, width=80, state="disabled")
        self.output_text.pack(pady=5)

        self.matrix_entries = []
        self.vector_entries = []

    def show_input_fields(self, event):
        for widget in self.input_frame.winfo_children():
            widget.destroy()

        method = self.method_var.get()

        if method == "Jacobi Method":
            self.matrix_entries = []
            self.vector_entries = []

            ttk.Label(self.input_frame, text="Enter A matrix:").grid(row=0, column=0, columnspan=3, pady=5)
            for i in range(3):
                row_entries = []
                for j in range(3):
                    entry = ttk.Entry(self.input_frame, width=5)
                    entry.grid(row=i + 1, column=j, padx=5, pady=5)
                    entry.insert(0, "0")  # Значение по умолчанию
                    row_entries.append(entry)
                self.matrix_entries.append(row_entries)

            ttk.Label(self.input_frame, text="Enter b vector:").grid(row=0, column=4, pady=5)
            for i in range(3):
                entry = ttk.Entry(self.input_frame, width=5)
                entry.grid(row=i + 1, column=4, padx=5, pady=5)
                entry.insert(0, "0")  # Значение по умолчанию
                self.vector_entries.append(entry)

        else:
            ttk.Label(self.input_frame, text="A:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
            self.a_entry = ttk.Entry(self.input_frame)
            self.a_entry.grid(row=0, column=1, padx=5, pady=5)
            self.a_entry.insert(0, "0")

            ttk.Label(self.input_frame, text="B:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
            self.b_entry = ttk.Entry(self.input_frame)
            self.b_entry.grid(row=1, column=1, padx=5, pady=5)
            self.b_entry.insert(0, "1")

    def run_method(self):
        method = self.method_var.get()
        if not method:
            messagebox.showerror("Error", "Choose method!")
            return

        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, f"Running {method}...\n")

        result_text = ""

        if method == "Graphical Method":
            a, b = self.a_entry.get(), self.b_entry.get()
            fig, result_text = execute_Task1(a, b, 1e-6)

        elif method == "Root-Finding Comparison":
            a, b = self.a_entry.get(), self.b_entry.get()
            result_text = execute_Task2(a, b, 1e-6)

        elif method == "Jacobi Method":
            result_text = execute_Task3(self.matrix_entries, self.vector_entries)

        self.output_text.insert(tk.END, result_text + "\n")
        self.output_text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumericalMethodsApp(root)
    root.mainloop()
