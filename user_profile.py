```python
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QFileDialog
from PyQt5.QtGui import QPixmap

class UserProfile(QWidget):
    def __init__(self, parent=None):
        super(UserProfile, self).__init__(parent)
        self.userProfileData = {
            "name": "",
            "avatar": "",
            "bio": ""
        }
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.name_label = QLabel("Name: ")
        self.name_input = QLineEdit()
        self.name_input.textChanged.connect(self.update_name)

        self.avatar_label = QLabel("Avatar: ")
        self.avatar_button = QPushButton("Choose Avatar")
        self.avatar_button.clicked.connect(self.choose_avatar)

        self.bio_label = QLabel("Bio: ")
        self.bio_input = QLineEdit()
        self.bio_input.textChanged.connect(self.update_bio)

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.avatar_label)
        self.layout.addWidget(self.avatar_button)
        self.layout.addWidget(self.bio_label)
        self.layout.addWidget(self.bio_input)

        self.setLayout(self.layout)

    def update_name(self, text):
        self.userProfileData["name"] = text

    def choose_avatar(self):
        file_dialog = QFileDialog()
        file_path = file_dialog.getOpenFileName()
        if file_path[0]:
            self.userProfileData["avatar"] = file_path[0]
            pixmap = QPixmap(self.userProfileData["avatar"])
            self.avatar_label.setPixmap(pixmap)

    def update_bio(self, text):
        self.userProfileData["bio"] = text
```