```python
import re
from chat_history import chatHistoryData

class Search:
    def __init__(self):
        self.data = chatHistoryData

    def search_chat(self, keyword, filter_options=None):
        results = []
        for chat in self.data:
            if re.search(keyword, chat['message'], re.I):
                if filter_options:
                    if self.check_filters(chat, filter_options):
                        results.append(chat)
                else:
                    results.append(chat)
        return results

    def check_filters(self, chat, filter_options):
        for key, value in filter_options.items():
            if key in chat:
                if isinstance(value, list):
                    if chat[key] not in value:
                        return False
                else:
                    if chat[key] != value:
                        return False
            else:
                return False
        return True

search = Search()
```
