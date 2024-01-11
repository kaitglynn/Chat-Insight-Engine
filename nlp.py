```python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from googletrans import Translator

class NLP:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.translator = Translator()

    def analyze_sentiment(self, text):
        sentiment_score = self.sia.polarity_scores(text)
        return sentiment_score

    def translate_text(self, text, dest_language):
        translation = self.translator.translate(text, dest=dest_language)
        return translation.text

nlp = NLP()
```