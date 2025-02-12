import tkinter as tk
from tkinter import ttk, messagebox
from Task1 import solve_task1  # Импорт модуля с задачей

class NumericalMethodsApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Numerical Methods")
        self.geometry("500x400")

        # Выбор задачи
        tk.Label(self, text="Выберите задачу:").pack(pady=5)

        self.task_selector = ttk.Combobox(self, state="readonly")
        self.task_selector["values"] = [
            "Task 1: Root-Finding (Bisection Method)",
            "Task 2: Other Methods (Not Implemented)"
        ]
        self.task_selector.current(0)
        self.task_selector.pack(pady=5)

        # Поля ввода
        self.create_input_field("Введите a:", "input_entry1")
        self.create_input_field("Введите b:", "input_entry2")

        # Кнопка "Решить"
        self.run_button = tk.Button(self, text="Решить", command=self.solve_task)
        self.run_button.pack(pady=10)

        # Поле вывода результата
        self.result_output = tk.Text(self, height=5, width=50, state="disabled")
        self.result_output.pack(pady=5)

    def create_input_field(self, label_text, entry_attr):
        tk.Label(self, text=label_text).pack()
        entry = tk.Entry(self)
        entry.pack(pady=5)
        setattr(self, entry_attr, entry)

    def solve_task(self):
        task_index = self.task_selector.current()
        try:
            a = float(self.input_entry1.get().strip())
            b = float(self.input_entry2.get().strip())
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числа для a и b")
            return

        if task_index == 0:
            result = solve_task1(a, b)
        else:
            result = "Эта задача еще не подключена."

        self.display_result(result)

    def display_result(self, result):
        self.result_output.config(state="normal")
        self.result_output.delete("1.0", tk.END)
        self.result_output.insert(tk.END, str(result))
        self.result_output.config(state="disabled")

if __name__ == "__main__":
    app = NumericalMethodsApp()
    app.mainloop()
