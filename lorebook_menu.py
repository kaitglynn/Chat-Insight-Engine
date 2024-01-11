```python
import tkinter as tk
from tkinter import ttk

class LorebookMenu:
    def __init__(self, root):
        self.root = root
        self.lorebookData = []

    def load_lorebook_data(self, lorebookData):
        self.lorebookData = lorebookData

    def display_lorebook_menu(self):
        lorebook_frame = tk.Frame(self.root)
        lorebook_frame.pack(fill='both', expand=True)

        lorebook_tree = ttk.Treeview(lorebook_frame)
        lorebook_tree['columns'] = ('Title', 'Content')

        lorebook_tree.column('#0', width=0, stretch='NO')
        lorebook_tree.column('Title', anchor='w', width=100)
        lorebook_tree.column('Content', anchor='w', width=400)

        lorebook_tree.heading('#0', text='', anchor='w')
        lorebook_tree.heading('Title', text='Title', anchor='w')
        lorebook_tree.heading('Content', text='Content', anchor='w')

        for lore in self.lorebookData:
            lorebook_tree.insert(parent='', index='end', iid=lore['id'], text='', values=(lore['title'], lore['content']))

        lorebook_tree.pack(fill='both', expand=True)

        return lorebook_frame
```