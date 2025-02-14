import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Task1, Task2, Task3, Task4, Task5, Task6, Task7, Task8

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
    diagonally_dominant,root = Task3.run(A, b, x0, tol=1e-6, max_iter=100)
    
    return f"Diagonally Dominant: {diagonally_dominant}\nRoot: {np.round(root, 6)}"

def execute_Task4(A_entries):
    try:
        A = np.array([[float(A_entries[i][j].get()) for j in range(3)] for i in range(3)])
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
        return None

    A_inv, A_inv_numpy, difference = Task4.run(A)
    
    return f"Inverse matrix (iteratively):\n{A_inv}\n\nInverse matrix (numpy.linalg.inv):\n{A_inv_numpy}\nDifference between iterative and numpy results:\n{difference}"

def execute_Task5(x_entries, y_entries):
    try:
        x = np.array([float(entry.get()) for entry in x_entries])
        y = np.array([float(entry.get()) for entry in y_entries])
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
        return None

    fig = Task5.run(x, y) 

    return fig

def execute_Task6(x_entries, y_entries):
    try:
        x = np.array([float(entry.get()) for entry in x_entries])
        y = np.array([float(entry.get()) for entry in y_entries])
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
        return None

    dy_dx = Task6.run(x, y)

    return f"dy/dx at x=1: {dy_dx}"

def execute_Task7(x1, x2):
    try:
        x1, x2 = float(x1), float(x2)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
        return None

    taylor_series, y_01, y_02 = Task7.run(x1, x2) 
    return f"Taylor series:\n{taylor_series}\ny({x1}) ≈ {y_01}\ny({x2}) ≈ {y_02}"

def execute_Task8(a, b, n):
    try:
        a, b, n = int(a), int(b), int(n)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
        return None
    
    I, exact_value, absolute_error = Task8.run(a, b, n)
    return f"Approximate value of the integral using Simpson's 3/8 Rule: {I}\nExact value of the integral: {exact_value}\nAbsolute error: {absolute_error}"


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
            "Matrix Inversion",
            "Linear Curve Fitting",
            "Newton’s Forward Difference",
            "Taylor Series Method",
            "Simpson's 3/8 Rule"
        )
        self.method_combobox.pack()
        self.method_combobox.bind("<<ComboboxSelected>>", self.show_input_fields)

        self.input_frame = ttk.Frame(root)
        self.input_frame.pack(pady=10)

        self.output_text = tk.Text(root, height=8, width=100, state="disabled")
        self.output_text.pack(pady=5)

        self.canvas_frame = ttk.Frame(root)
        self.canvas_frame.pack(pady=20)

        self.run_button = ttk.Button(root, text="Run Method", command=self.run_method)
        self.run_button.pack()

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
                    entry.insert(0, "0")
                    row_entries.append(entry)
                self.matrix_entries.append(row_entries)

            ttk.Label(self.input_frame, text="Enter b vector:").grid(row=0, column=4, pady=5)
            for i in range(3):
                entry = ttk.Entry(self.input_frame, width=5)
                entry.grid(row=i + 1, column=4, padx=5, pady=5)
                entry.insert(0, "0") 
                self.vector_entries.append(entry)

        elif method == "Matrix Inversion":
            self.matrix_entries = []
            ttk.Label(self.input_frame, text="Enter A matrix:").grid(row=0, column=0, columnspan=3, pady=5)
            for i in range(3):
                row_entries = []
                for j in range(3):
                    entry = ttk.Entry(self.input_frame, width=5)
                    entry.grid(row=i + 1, column=j, padx=5, pady=5)
                    entry.insert(0, "0") 
                    row_entries.append(entry)
                self.matrix_entries.append(row_entries)
            
        elif method == "Linear Curve Fitting":
            self.x_entries = []
            self.y_entries = []

            ttk.Label(self.input_frame, text="Enter x values:").grid(row=0, column=0, pady=5)
            for i in range(5):
                entry = ttk.Entry(self.input_frame, width=5)
                entry.grid(row=1, column=i, padx=5, pady=5)
                entry.insert(0, str(i + 1)) 
                self.x_entries.append(entry)

            ttk.Label(self.input_frame, text="Enter y values:").grid(row=2, column=0, pady=5)
            for i in range(5):
                entry = ttk.Entry(self.input_frame, width=5)
                entry.grid(row=3, column=i, padx=5, pady=5)
                entry.insert(0, str(5 + 3 * i)) 
                self.y_entries.append(entry)

        elif method == "Newton’s Forward Difference":
            self.x_entries = []
            self.y_entries = []

            ttk.Label(self.input_frame, text="Enter x values:").grid(row=0, column=0, pady=5)
            for i in range(3):
                entry = ttk.Entry(self.input_frame, width=5)
                entry.grid(row=1, column=i, padx=5, pady=5)
                entry.insert(0, str(i + 1)) 
                self.x_entries.append(entry)

            ttk.Label(self.input_frame, text="Enter y values:").grid(row=2, column=0, pady=5)
            for i in range(3):
                entry = ttk.Entry(self.input_frame, width=5)
                entry.grid(row=3, column=i, padx=5, pady=5)
                entry.insert(0, str(5 + 3 * i)) 
                self.y_entries.append(entry)

        elif method == "Taylor Series Method":
            ttk.Label(self.input_frame, text="Enter x1:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
            self.x1_entry = ttk.Entry(self.input_frame)
            self.x1_entry.grid(row=0, column=1, padx=5, pady=5)
            self.x1_entry.insert(0, "0.1")

            ttk.Label(self.input_frame, text="Enter x2:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
            self.x2_entry = ttk.Entry(self.input_frame)
            self.x2_entry.grid(row=1, column=1, padx=5, pady=5)
            self.x2_entry.insert(0, "0.2")

        elif method == "Simpson's 3/8 Rule":
            ttk.Label(self.input_frame, text="A:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
            self.a_entry = ttk.Entry(self.input_frame)
            self.a_entry.grid(row=0, column=1, padx=5, pady=5)
            self.a_entry.insert(0, "2")

            ttk.Label(self.input_frame, text="B:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
            self.b_entry = ttk.Entry(self.input_frame)
            self.b_entry.grid(row=1, column=1, padx=5, pady=5)
            self.b_entry.insert(0, "5")

            ttk.Label(self.input_frame, text="Subinterval:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
            self.n_entry = ttk.Entry(self.input_frame)
            self.n_entry.grid(row=2, column=1, padx=5, pady=5)
            self.n_entry.insert(0, "6")


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

        elif method == "Matrix Inversion":
            result_text = execute_Task4(self.matrix_entries)

        elif method == "Linear Curve Fitting":
            fig = execute_Task5(self.x_entries, self.y_entries)

        elif method == "Newton’s Forward Difference":
            result_text = execute_Task6(self.x_entries, self.y_entries)

        elif method == "Taylor Series Method":
            x1, x2 = self.x1_entry.get(), self.x2_entry.get()
            result_text = execute_Task7(x1, x2)

        elif method == "Simpson's 3/8 Rule":
            a, b, n = self.a_entry.get(), self.b_entry.get(), self.n_entry.get()
            result_text = execute_Task8(a, b, n)


        self.output_text.insert(tk.END, f"{result_text}\n")

        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        if fig:
            self.display_graph(fig) 

    def display_graph(self, fig):
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = NumericalMethodsApp(root)
    root.mainloop()
