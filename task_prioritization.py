```python
import heapq

class Task:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):
        return self.priority < other.priority

class TaskPrioritization:
    def __init__(self):
        self.tasks = []

    def add_task(self, priority, description):
        task = Task(priority, description)
        heapq.heappush(self.tasks, task)

    def get_next_task(self):
        if self.tasks:
            next_task = heapq.heappop(self.tasks)
            return next_task.description
        else:
            return None

task_prioritization = TaskPrioritization()

def prioritizeTask(priority, description):
    task_prioritization.add_task(priority, description)

def getNextTask():
    return task_prioritization.get_next_task()
```