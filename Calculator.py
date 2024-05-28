#-*- coding:cp1251 -*-
import tkinter as tk
from tkinter import ttk
import math

def show_calculator(event):
    figure = figure_var.get()
    for frame in frames.values():
        frame.grid_remove()

    if figure == "Треугольник":
        frames["triangle"].grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    elif figure == "Ромб":
        frames["rhombus"].grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    elif figure == "Трапеция":
        frames["trapezoid"].grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    elif figure == "Квадрат":
        frames["square"].grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    elif figure == "Прямоугольник":
        frames["rectangle"].grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    elif figure == "Параллелограмм":
        frames["parallelogram"].grid(row=1, column=1, columnspan=2, padx=10, pady=10)

def calculate_area():
    figure = figure_var.get()
    if figure == "Ромб":
        diagonal1 = float(diagonal1_entry.get())
        diagonal2 = float(diagonal2_entry.get())
        area = 0.5 * diagonal1 * diagonal2
        result_label.config(text=f"Площадь ромба: {area:.2f}")
    elif figure == "Треугольник":
        base = float(base_entry.get())
        height = float(height_entry.get())
        area = 0.5 * base * height 
        result_label.config(text=f"Площадь треугольника: {area:.2f}")
    elif figure == "Трапеция":
        base1 = float(base1_entry.get())
        base2 = float(base2_entry.get())
        height1 = float(height1_entry.get())
        area = 0.5 * (base1 + base2) * height1
        result_label.config(text=f"Площадь трапеции: {area:.2f}")
    elif figure == "Квадрат":
        side = float(side_entry.get())
        area = side ** 2
        result_label.config(text=f"Площадь квадрата: {area:.2f}")
    elif figure == "Прямоугольник":
        length = float(length_entry.get())
        width = float(width_entry.get())
        area = length * width
        result_label.config(text=f"Площадь прямоугольника: {area:.2f}")
    elif figure == "Параллелограмм":
        basepr = float(basepr_entry.get())
        heightpr = float(heightpr_entry.get())
        area = basepr * heightpr
        result_label.config(text=f"Площадь параллелограмма: {area:.2f}")

root = tk.Tk()
root.title("Калькулятор площади геометрических фигур")
root.geometry("500x250")

# Выбор фигуры
figure_label = ttk.Label(root, text="Выберите фигуру:")
figure_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

figure_var = tk.StringVar()
figure_combobox = ttk.Combobox(root, textvariable=figure_var, values=["Треугольник", "Ромб", "Трапеция", "Квадрат", "Прямоугольник", "Параллелограмм"])
figure_combobox.grid(row=0, column=1, padx=10, pady=10)
figure_combobox.bind("<<ComboboxSelected>>", show_calculator)

frames = {}

# Треугольник
frames["triangle"] = ttk.LabelFrame(root, text="Треугольник")

base_label = ttk.Label(frames["triangle"], text="Основание:")
base_label.grid(row=1, column=0, padx=5, pady=5)
base_entry = ttk.Entry(frames["triangle"])
base_entry.grid(row=1, column=1, padx=5, pady=5)

height_label = ttk.Label(frames["triangle"], text="Высота:")
height_label.grid(row=2, column=0, padx=5, pady=5)
height_entry = ttk.Entry(frames["triangle"])
height_entry.grid(row=2, column=1, padx=5, pady=5)

# Параллелограмм
frames["parallelogram"] = ttk.LabelFrame(root, text="Параллелограмм")

basepr_label = ttk.Label(frames["parallelogram"], text="Основание:")
basepr_label.grid(row=1, column=0, padx=5, pady=5)
basepr_entry = ttk.Entry(frames["parallelogram"])
basepr_entry.grid(row=1, column=1, padx=5, pady=5)

heightpr_label = ttk.Label(frames["parallelogram"], text="Высота:")
heightpr_label.grid(row=2, column=0, padx=5, pady=5)
heightpr_entry = ttk.Entry(frames["parallelogram"])
heightpr_entry.grid(row=2, column=1, padx=5, pady=5)


# Ромб
frames["rhombus"] = ttk.LabelFrame(root, text="Ромб")

diagonal1_label = ttk.Label(frames["rhombus"], text="Диагональ 1:")
diagonal1_label.grid(row=0, column=0, padx=5, pady=5)
diagonal1_entry = ttk.Entry(frames["rhombus"])
diagonal1_entry.grid(row=0, column=1, padx=5, pady=5)

diagonal2_label = ttk.Label(frames["rhombus"], text="Диагональ 2:")
diagonal2_label.grid(row=1, column=0, padx=5, pady=5)
diagonal2_entry = ttk.Entry(frames["rhombus"])
diagonal2_entry.grid(row=1, column=1, padx=5, pady=5)

# Трапеция
frames["trapezoid"] = ttk.LabelFrame(root, text="Трапеция")

base1_label = ttk.Label(frames["trapezoid"], text="Основание 1:")
base1_label.grid(row=0, column=0, padx=5, pady=5)
base1_entry = ttk.Entry(frames["trapezoid"])
base1_entry.grid(row=0, column=1, padx=5, pady=5)

base2_label = ttk.Label(frames["trapezoid"], text="Основание 2:")
base2_label.grid(row=1, column=0, padx=5, pady=5)
base2_entry = ttk.Entry(frames["trapezoid"])
base2_entry.grid(row=1, column=1, padx=5, pady=5)

height1_label = ttk.Label(frames["trapezoid"], text="Высота:")
height1_label.grid(row=2, column=0, padx=5, pady=5)
height1_entry = ttk.Entry(frames["trapezoid"])
height1_entry.grid(row=2, column=1, padx=5, pady=5)

# Квадрат
frames["square"] = ttk.LabelFrame(root, text="Квадрат")

side_label = ttk.Label(frames["square"], text="Сторона:")
side_label.grid(row=0, column=0, padx=5, pady=5)
side_entry = ttk.Entry(frames["square"])
side_entry.grid(row=0, column=1, padx=5, pady=5)

# Прямоугольник
frames["rectangle"] = ttk.LabelFrame(root, text="Прямоугольник")

length_label = ttk.Label(frames["rectangle"], text="Длина:")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = ttk.Entry(frames["rectangle"])
length_entry.grid(row=0, column=1, padx=5, pady=5)

width_label = ttk.Label(frames["rectangle"], text="Ширина:")
width_label.grid(row=1, column=0, padx=5, pady=5)
width_entry = ttk.Entry(frames["rectangle"])
width_entry.grid(row=1, column=1, padx=5, pady=5)

# Кнопка расчета и результат
calculate_button = ttk.Button(root, text="Рассчитать", command=calculate_area)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()