```python
from google.cloud import translate_v2 as translate

class TranslationService:
    def __init__(self):
        self.translate_client = translate.Client()

    def translate_text(self, text, target_language):
        if isinstance(text, bytes):
            text = text.decode("utf-8")

        result = self.translate_client.translate(text, target_language)

        return result["input"], result["translatedText"], result["detectedSourceLanguage"]

translation_service = TranslationService()
```