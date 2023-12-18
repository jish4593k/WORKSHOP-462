import tkinter as tk
from tkinter import Label, Button
import torch
import seaborn as sns
import matplotlib.pyplot as plt




class App:
    def __init__(self, master):
        self.master = master
        master.title("PyTorch and Tkinter App")

        self.random_tensor = generate_random_tensor()

        self.label = Label(master, text="Tensor Operations and Visualization")
        self.label.pack()

        self.sum_button = Button(master, text="Calculate Sum", command=self.calculate_sum)
        self.sum_button.pack()

        self.mean_button = Button(master, text="Calculate Mean", command=self.calculate_mean)
        self.mean_button.pack()

        self.visualize_button = Button(master, text="Visualize Tensor", command=self.visualize)
        self.visualize_button.pack()

    def calculate_sum(self):
        tensor_sum, _ = tensor_operations(self.random_tensor)
        result_label = Label(self.master, text=f"Sum of tensor elements: {tensor_sum}")
        result_label.pack()

    def calculate_mean(self):
        _, tensor_mean = tensor_operations(self.random_tensor)
        result_label = Label(self.master, text=f"Mean of tensor elements: {tensor_mean}")
        result_label.pack()

    def visualize(self):
        visualize_tensor(self.random_tensor)

if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
