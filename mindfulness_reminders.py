```python
import time
from plyer import notification

class MindfulnessReminder:
    def __init__(self, mindfulnessData):
        self.mindfulnessData = mindfulnessData

    def remind(self):
        while True:
            for data in self.mindfulnessData:
                notification.notify(
                    title = data['title'],
                    message = data['message'],
                    timeout = 10
                )
                time.sleep(data['interval'])

if __name__ == "__main__":
    mindfulnessData = [
        {
            'title': 'Take a deep breath',
            'message': 'Remember to breathe deeply and relax.',
            'interval': 3600
        },
        {
            'title': 'Stretch',
            'message': 'Take a moment to stretch and move around.',
            'interval': 7200
        }
    ]

    mindfulnessReminder = MindfulnessReminder(mindfulnessData)
    mindfulnessReminder.remind()
```