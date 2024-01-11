```python
import tkinter as tk
from tkinter import messagebox

def getHelpSupport():
    # Create a new window
    help_window = tk.Toplevel()
    help_window.title("Help & Support")

    # Create a label for the window
    label = tk.Label(help_window, text="Welcome to Help & Support!")
    label.pack(padx=10, pady=10)

    # Create a text box for the window
    text_box = tk.Text(help_window, width=50, height=10)
    text_box.pack(padx=10, pady=10)

    # Create a submit button for the window
    submit_button = tk.Button(help_window, text="Submit", command=lambda: submit_query(text_box.get("1.0", "end-1c")))
    submit_button.pack(pady=10)

def submit_query(query):
    # Here you can add functionality to handle the query, like sending it to an API or searching in a database
    # For now, we will just show a message box
    messagebox.showinfo("Query submitted", "Your query has been submitted. We will get back to you as soon as possible.")
```