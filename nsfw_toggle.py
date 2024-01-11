```python
class NSFWToggle:
    def __init__(self):
        self.nsfwToggle = False

    def get_nsfw_status(self):
        return self.nsfwToggle

    def toggle_nsfw(self):
        self.nsfwToggle = not self.nsfwToggle
        return self.nsfwToggle

nsfw_toggle = NSFWToggle()

def toggleNSFW():
    nsfw_status = nsfw_toggle.toggle_nsfw()
    if nsfw_status:
        print("NSFW content is now enabled.")
    else:
        print("NSFW content is now disabled.")
    return nsfw_status
```