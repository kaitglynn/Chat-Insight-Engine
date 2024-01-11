```python
import json

class ChatHistory:
    def __init__(self):
        self.chatHistoryData = []

    def load_chat_history(self, filename):
        with open(filename, 'r') as file:
            self.chatHistoryData = json.load(file)

    def save_chat_history(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.chatHistoryData, file)

    def add_message(self, message):
        self.chatHistoryData.append(message)

    def search_chat_history(self, keyword):
        return [message for message in self.chatHistoryData if keyword in message]

    def filter_chat_history(self, date=None, file_type=None):
        if date:
            return [message for message in self.chatHistoryData if message['date'] == date]
        elif file_type:
            return [message for message in self.chatHistoryData if message['file_type'] == file_type]
        else:
            return self.chatHistoryData

if __name__ == "__main__":
    chat_history = ChatHistory()
    chat_history.load_chat_history('chat_history.json')
    chat_history.add_message({'user': 'User1', 'message': 'Hello, bot!', 'date': '2022-01-01', 'file_type': 'text'})
    chat_history.save_chat_history('chat_history.json')
    print(chat_history.search_chat_history('Hello'))
    print(chat_history.filter_chat_history(date='2022-01-01'))
```
