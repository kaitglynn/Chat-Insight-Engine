```python
import tkinter as tk
from chat_interface import ChatInterface
from voice_chat import VoiceChat
from user_profile import UserProfile
from bot_profile import BotProfile
from file_sharing import FileSharing
from chat_history import ChatHistory
from search import Search
from notifications import Notifications
from themes import Themes
from help_support import HelpSupport

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Insight Engine")
        self.create_widgets()

    def create_widgets(self):
        self.chat_interface = ChatInterface(self.window)
        self.voice_chat = VoiceChat(self.window)
        self.user_profile = UserProfile(self.window)
        self.bot_profile = BotProfile(self.window)
        self.file_sharing = FileSharing(self.window)
        self.chat_history = ChatHistory(self.window)
        self.search = Search(self.window)
        self.notifications = Notifications(self.window)
        self.themes = Themes(self.window)
        self.help_support = HelpSupport(self.window)

        self.navigation_bar = tk.Menu(self.window)
        self.navigation_bar.add_command(label="Home", command=self.chat_interface.display)
        self.navigation_bar.add_command(label="Voice Chat", command=self.voice_chat.display)
        self.navigation_bar.add_command(label="Profile", command=self.user_profile.display)
        self.navigation_bar.add_command(label="Settings", command=self.themes.display)
        self.window.config(menu=self.navigation_bar)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = GUI()
    gui.run()
```