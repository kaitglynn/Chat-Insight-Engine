```python
import tkinter as tk
from tkinter import ttk

# Define the theme data schema
class ThemeData:
    def __init__(self, theme_name, bg_color, fg_color, font):
        self.theme_name = theme_name
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.font = font

# Define the function to change the theme
def change_theme(root, theme_data):
    root.configure(bg=theme_data.bg_color)
    for widget in root.winfo_children():
        if isinstance(widget, (tk.Label, tk.Button, ttk.Combobox)):
            widget.configure(bg=theme_data.bg_color, fg=theme_data.fg_color, font=theme_data.font)

# Define the function to load the theme data
def load_theme_data(theme_name):
    # Here we just define some dummy data, in real application, the theme data should be loaded from a database or a file
    if theme_name == "Light":
        return ThemeData("Light", "white", "black", ("Arial", 12))
    elif theme_name == "Dark":
        return ThemeData("Dark", "black", "white", ("Arial", 12))
    else:
        return ThemeData("Default", "SystemButtonFace", "SystemButtonText", ("Arial", 12))

# Define the function to apply the theme
def apply_theme(root, theme_name):
    theme_data = load_theme_data(theme_name)
    change_theme(root, theme_data)
    themeData = theme_data
```
