```python
import datetime
from typing import Dict

class Activity:
    def __init__(self, activity_type: str, timestamp: datetime.datetime):
        self.activity_type = activity_type
        self.timestamp = timestamp

class ActivityTracker:
    def __init__(self):
        self.activities = []

    def track_activity(self, activity_type: str):
        activity = Activity(activity_type, datetime.datetime.now())
        self.activities.append(activity)

    def get_activities(self) -> Dict[str, int]:
        activity_count = {}
        for activity in self.activities:
            if activity.activity_type in activity_count:
                activity_count[activity.activity_type] += 1
            else:
                activity_count[activity.activity_type] = 1
        return activity_count

activity_tracker = ActivityTracker()

def track_activity(activity_type: str):
    activity_tracker.track_activity(activity_type)

def get_activity_data():
    return activity_tracker.get_activities()
```