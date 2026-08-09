# Task 5 : - Build 2–3 reusable plotting functions (a tiny personal visualization module).

import matplotlib.pyplot as plt

# Helper function to save figures
def _save_figure(save_path):
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

# Bar Chart Function

def bar_chart(labels, values, title="Bar Chart",
              xlabel="Categories", ylabel="Values",
              color="skyblue", save_path=None):
    """Create a simple bar chart from category labels and numeric values."""
    plt.figure(figsize=(8, 5))
    plt.bar(labels, values, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    _save_figure(save_path)
    plt.show()

# Line Chart Function

def line_chart(labels, values, title="Line Chart",
               xlabel="X-Axis", ylabel="Y-Axis",
               color="blue", marker="o", save_path=None):
    """Create a simple line chart from x labels and y values."""
    plt.figure(figsize=(8, 5))
    plt.plot(labels, values, color=color, marker=marker, linewidth=2)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    _save_figure(save_path)
    plt.show()

# Pie Chart Function

def pie_chart(labels, values, title="Pie Chart", save_path=None):
    """Create a simple pie chart using labels and numeric values."""
    plt.figure(figsize=(7, 7))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title(title)
    _save_figure(save_path)
    plt.show()
