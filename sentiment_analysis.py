```python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalysis:
    def __init__(self):
        nltk.download('vader_lexicon')
        self.sia = SentimentIntensityAnalyzer()

    def analyze_sentiment(self, text):
        sentiment_score = self.sia.polarity_scores(text)
        return sentiment_score

    def get_sentiment(self, text):
        sentiment_score = self.analyze_sentiment(text)
        if sentiment_score['compound'] > 0.05:
            return 'Positive'
        elif sentiment_score['compound'] < -0.05:
            return 'Negative'
        else:
            return 'Neutral'
```