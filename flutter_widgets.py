```python
import flutter

class MainScreen(flutter.Widget):
    def build(self, context):
        return flutter.Scaffold(
            appBar: flutter.AppBar(
                title: flutter.Text('Insight Engine'),
            ),
            body: flutter.Row(
                children: [
                    UserSection(),
                    BotSection(),
                ],
            ),
            bottomNavigationBar: NavigationBar(),
        )


class UserSection(flutter.Widget):
    def build(self, context):
        return flutter.Expanded(
            child: flutter.ListView.builder(
                itemCount: len(userProfileData),
                itemBuilder: (context, index) {
                    return flutter.Text(userProfileData[index])
                },
            ),
        )


class BotSection(flutter.Widget):
    def build(self, context):
        return flutter.Expanded(
            child: flutter.ListView.builder(
                itemCount: len(botProfileData),
                itemBuilder: (context, index) {
                    return flutter.Text(botProfileData[index])
                },
            ),
        )


class NavigationBar(flutter.Widget):
    def build(self, context):
        return flutter.BottomNavigationBar(
            items: [
                flutter.BottomNavigationBarItem(
                    icon: flutter.Icon(flutter.Icons.home),
                    label: 'Home',
                ),
                flutter.BottomNavigationBarItem(
                    icon: flutter.Icon(flutter.Icons.mic),
                    label: 'Voice Chat',
                ),
                flutter.BottomNavigationBarItem(
                    icon: flutter.Icon(flutter.Icons.person),
                    label: 'Profile',
                ),
                flutter.BottomNavigationBarItem(
                    icon: flutter.Icon(flutter.Icons.settings),
                    label: 'Settings',
                ),
            ],
        )
```
