#-*- coding:cp1251 -*-
import unittest
from Calculator import show_calculator
from Calculator import calculate_area
from tkinter import ttk
import tkinter as tk


class TestCalculator1(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.figure_var = tk.StringVar()
        self.figure_combobox = ttk.Combobox(self.root, textvariable=self.figure_var, values=["Треугольник", "Ромб", "Трапеция", "Квадрат", "Прямоугольник", "Параллелограмм"])
        self.figure_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.figure_combobox.bind("<<ComboboxSelected>>", show_calculator)

    def test_figure_selection(self):
        self.figure_var.set("Треугольник")
        self.figure_combobox.event_generate("<<ComboboxSelected>>")
        self.assertEqual(self.figure_combobox.get(), "Треугольник")
        self.assertEqual(len(self.figure_combobox.get()), 10)

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()
    
