```python
import os
import shutil

class FileManager:
    def __init__(self):
        self.fileData = {}

    def save_file(self, file, destination):
        try:
            shutil.copy(file, destination)
            self.fileData[file] = destination
            return True
        except Exception as e:
            print(f"An error occurred while saving the file: {e}")
            return False

    def delete_file(self, file):
        try:
            os.remove(file)
            del self.fileData[file]
            return True
        except Exception as e:
            print(f"An error occurred while deleting the file: {e}")
            return False

    def move_file(self, file, destination):
        try:
            shutil.move(file, destination)
            self.fileData[file] = destination
            return True
        except Exception as e:
            print(f"An error occurred while moving the file: {e}")
            return False

    def get_file_location(self, file):
        try:
            return self.fileData[file]
        except KeyError:
            print(f"No data found for the file: {file}")
            return None
```