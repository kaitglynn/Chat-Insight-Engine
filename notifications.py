```python
import time
from plyer import notification

class Notifications:
    def __init__(self):
        self.notificationData = []

    def add_notification(self, title, message, timeout=10):
        self.notificationData.append({
            'title': title,
            'message': message,
            'timeout': timeout
        })

    def display_notifications(self):
        for data in self.notificationData:
            notification.notify(
                title=data['title'],
                message=data['message'],
                timeout=data['timeout']
            )
            time.sleep(data['timeout'])

    def clear_notifications(self):
        self.notificationData.clear()

notifications = Notifications()
```