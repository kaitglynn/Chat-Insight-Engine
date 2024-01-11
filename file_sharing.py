```python
import os
from tkinter import filedialog
from tkinter import messagebox

class FileSharing:
    def __init__(self):
        self.fileData = {}

    def open_file_dialog(self):
        filename = filedialog.askopenfilename(initialdir = "/", title = "Select file",
                                              filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        if filename:
            self.fileData['filename'] = filename
            self.fileData['filetype'] = os.path.splitext(filename)[1]
            self.preview_file()

    def preview_file(self):
        if self.fileData['filetype'] in ['.jpg', '.png', '.gif']:
            # Display image preview
            pass
        elif self.fileData['filetype'] in ['.txt', '.docx', '.pdf']:
            # Display text file preview
            pass
        else:
            messagebox.showinfo("Preview not available", "Preview is not available for the selected file type.")

    def share_file(self):
        if 'filename' in self.fileData:
            # Code to share the file goes here
            pass
        else:
            messagebox.showerror("No file selected", "Please select a file to share.")

file_sharing = FileSharing()
```
