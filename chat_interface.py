```python
import tkinter as tk
from tkinter import ttk

class ChatInterface:
    def __init__(self, root):
        self.root = root
        self.create_chat_interface()

    def create_chat_interface(self):
        self.chat_frame = tk.Frame(self.root)
        self.chat_frame.pack(fill="both", expand=True)

        self.text_chat = tk.Text(self.chat_frame, bg="white", fg="black")
        self.text_chat.pack(fill="both", expand=True)

        self.entry_frame = tk.Frame(self.chat_frame)
        self.entry_frame.pack(fill="x")

        self.message_entry = tk.Entry(self.entry_frame, bg="white", fg="black")
        self.message_entry.pack(side="left", fill="x", expand=True)

        self.send_button = tk.Button(self.entry_frame, text="Send", command=self.send_message)
        self.send_button.pack(side="right")

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.text_chat.insert("end", "You: " + message + "\n")
            self.message_entry.delete(0, "end")

            # Here you can add the function to process the message and get a response from the bot
            bot_response = self.get_bot_response(message)
            self.text_chat.insert("end", "Bot: " + bot_response + "\n")

    def get_bot_response(self, message):
        # This function should be implemented in another file (like nlp.py) and imported here
        # For now, it just echoes the user's message
        return message

if __name__ == "__main__":
    root = tk.Tk()
    chat_interface = ChatInterface(root)
    root.mainloop()
```