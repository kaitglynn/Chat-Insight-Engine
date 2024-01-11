```python
import tkinter as tk
from PIL import ImageTk, Image

class BotAvatar:
    def __init__(self, root):
        self.root = root
        self.avatar_frame = tk.Frame(self.root)
        self.avatar_frame.pack()

        self.avatar_img = ImageTk.PhotoImage(Image.open("bot_avatar.png"))
        self.avatar_label = tk.Label(self.avatar_frame, image=self.avatar_img)
        self.avatar_label.pack()

    def change_expression(self, expression):
        self.avatar_img = ImageTk.PhotoImage(Image.open(f"bot_avatar_{expression}.png"))
        self.avatar_label.config(image=self.avatar_img)
        self.avatar_label.image = self.avatar_img

if __name__ == "__main__":
    root = tk.Tk()
    bot_avatar = BotAvatar(root)
    root.mainloop()
```