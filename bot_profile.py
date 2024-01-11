```python
class BotProfile:
    def __init__(self):
        self.botProfileData = {
            "name": "Mistral 7",
            "avatar": "default_avatar.png",
            "bio": "I'm your AI assistant, here to help you!"
        }

    def display_bot_profile(self):
        print(f"Name: {self.botProfileData['name']}")
        print(f"Avatar: {self.botProfileData['avatar']}")
        print(f"Bio: {self.botProfileData['bio']}")

    def edit_bot_profile(self, name=None, avatar=None, bio=None):
        if name:
            self.botProfileData['name'] = name
        if avatar:
            self.botProfileData['avatar'] = avatar
        if bio:
            self.botProfileData['bio'] = bio
        self.display_bot_profile()

if __name__ == "__main__":
    bot_profile = BotProfile()
    bot_profile.display_bot_profile()
    bot_profile.edit_bot_profile(name="Mistral 7.1", bio="I'm your updated AI assistant, even more helpful!")
```