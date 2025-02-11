import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QComboBox, QPushButton, 
    QVBoxLayout, QWidget, QTextEdit, QLineEdit, QHBoxLayout
)
import matplotlib.pyplot as plt
import numpy as np
from Task1 import solve_task1  # Импортируем функцию решения первой задачи

class NumericalMethodsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Numerical Methods")
        self.setGeometry(100, 100, 600, 500)

        # Виджеты
        self.label = QLabel("Выберите задачу:")
        self.task_selector = QComboBox()
        self.task_selector.addItems([
            "Task 1: Graphical Method",
            "Task 2: Root-Finding Methods",
            "Task 3: Jacobi Method",
            "Task 4: Matrix Inversion",
            "Task 5: Curve Fitting",
            "Task 6: Derivative Approximation",
            "Task 7: Taylor Series Method",
            "Task 8: Simpson's Rule"
        ])

        # Поля ввода чисел
        self.a_input = QLineEdit()
        self.a_input.setPlaceholderText("Введите a (например, 0)")

        self.b_input = QLineEdit()
        self.b_input.setPlaceholderText("Введите b (например, 1)")


        # Кнопка запуска
        self.run_button = QPushButton("Решить")
        self.run_button.clicked.connect(self.solve_task)

        # Поле вывода результата
        self.result_output = QTextEdit()
        self.result_output.setReadOnly(True)

        # Размещение виджетов
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.task_selector)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.a_input)
        input_layout.addWidget(self.b_input)
        layout.addLayout(input_layout)

        layout.addWidget(self.run_button)
        layout.addWidget(self.result_output)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def solve_task(self):
        task_index = self.task_selector.currentIndex()

        if task_index == 0:  # Task 1
            try:
                a = float(self.a_input.text())
                b = float(self.b_input.text())

                # Вызываем задачу 1 и получаем результат
                result, fig = solve_task1(a, b, 1e-6)

                # Показываем график
                fig.show()

                # Вывод результата в текстовое поле
                self.result_output.setText(result)

            except ValueError:
                self.result_output.setText("Ошибка: Введите корректные числа!")

        else:
            self.result_output.setText("Эта задача еще не подключена.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NumericalMethodsApp()
    window.show()
    sys.exit(app.exec())
