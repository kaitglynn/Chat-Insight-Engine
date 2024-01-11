```python
import requests
from bs4 import BeautifulSoup

def scrapeWeb(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except Exception as err:
        print(f'Other error occurred: {err}')
        return None
    else:
        return BeautifulSoup(response.text, 'html.parser')

def extractText(soup):
    if soup is None:
        return None
    else:
        return ' '.join([p.text for p in soup.find_all('p')])

def extractLinks(soup):
    if soup is None:
        return None
    else:
        return [a['href'] for a in soup.find_all('a', href=True)]

def extractImages(soup):
    if soup is None:
        return None
    else:
        return [img['src'] for img in soup.find_all('img', src=True)]
```