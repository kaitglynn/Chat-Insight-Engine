```python
import requests
from bs4 import BeautifulSoup

class MusicRecommendations:
    def __init__(self):
        self.musicData = []

    def get_recommendations(self, genre):
        url = f"https://www.billboard.com/charts/{genre}-songs"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        songs = soup.find_all('span', class_='chart-element__information__song text--truncate color--primary')
        artists = soup.find_all('span', class_='chart-element__information__artist text--truncate color--secondary')

        for i in range(len(songs)):
            self.musicData.append({
                'song': songs[i].text,
                'artist': artists[i].text
            })

        return self.musicData

music_recommendations = MusicRecommendations()
musicData = music_recommendations.get_recommendations('rock')
```