```python
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/presentations.readonly']

def get_google_slides_service():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    try:
        service = build('slides', 'v1', credentials=creds)
        return service
    except Exception as e:
        print(e)
        return None

def get_presentation(presentation_id):
    service = get_google_slides_service()
    if service:
        presentation = service.presentations().get(presentationId=presentation_id).execute()
        return presentation
    else:
        return None

def get_slide_text(presentation_id, slide_id):
    presentation = get_presentation(presentation_id)
    if presentation:
        for slide in presentation['slides']:
            if slide['objectId'] == slide_id:
                for element in slide['pageElements']:
                    if 'shape' in element and 'text' in element['shape']:
                        return element['shape']['text']['textElements'][0]['textRun']['content']
    return None
```