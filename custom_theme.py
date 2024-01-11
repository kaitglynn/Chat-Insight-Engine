```python
import tkinter as tk
from tkinter import ttk

class CustomTheme:
    def __init__(self, root):
        self.root = root
        self.themeData = {}

    def load_theme(self, theme_name):
        try:
            with open(f'{theme_name}.json', 'r') as file:
                self.themeData = json.load(file)
        except FileNotFoundError:
            print("Theme file not found. Loading default theme.")
            self.themeData = self.default_theme()

        self.apply_theme()

    def default_theme(self):
        return {
            "background": "#FFFFFF",
            "foreground": "#000000",
            "button_color": "#DDDDDD",
            "button_font_color": "#000000",
            "highlight_color": "#FF0000"
        }

    def apply_theme(self):
        self.root.configure(bg=self.themeData['background'])
        style = ttk.Style()
        style.configure("TButton",
                        foreground=self.themeData['button_font_color'],
                        background=self.themeData['button_color'])
        style.map("TButton",
                  background=[('active', self.themeData['highlight_color'])])

    def change_theme(self, theme_name):
        self.load_theme(theme_name)
        self.apply_theme()

if __name__ == "__main__":
    root = tk.Tk()
    theme = CustomTheme(root)
    theme.change_theme("dark_mode")
    tk.Button(root, text="Test Button").pack()
    root.mainloop()
```