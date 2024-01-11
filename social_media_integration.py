```python
import requests
from social_media_schema import SocialMediaSchema

class SocialMediaIntegration:
    def __init__(self):
        self.socialMediaData = SocialMediaSchema()

    def integrateSocialMedia(self, platform, user_id):
        if platform.lower() == "facebook":
            self.socialMediaData.facebook_id = user_id
        elif platform.lower() == "twitter":
            self.socialMediaData.twitter_id = user_id
        elif platform.lower() == "instagram":
            self.socialMediaData.instagram_id = user_id
        else:
            print("Unsupported platform")

    def postToSocialMedia(self, platform, message):
        if platform.lower() == "facebook":
            self.postToFacebook(message)
        elif platform.lower() == "twitter":
            self.postToTwitter(message)
        elif platform.lower() == "instagram":
            self.postToInstagram(message)
        else:
            print("Unsupported platform")

    def postToFacebook(self, message):
        # This is a placeholder function. Actual implementation would require use of Facebook's API.
        print(f"Posting to Facebook: {message}")

    def postToTwitter(self, message):
        # This is a placeholder function. Actual implementation would require use of Twitter's API.
        print(f"Posting to Twitter: {message}")

    def postToInstagram(self, message):
        # This is a placeholder function. Actual implementation would require use of Instagram's API.
        print(f"Posting to Instagram: {message}")

socialMediaIntegration = SocialMediaIntegration()
socialMediaIntegration.integrateSocialMedia("facebook", "123456789")
socialMediaIntegration.postToSocialMedia("facebook", "Hello, world!")
```