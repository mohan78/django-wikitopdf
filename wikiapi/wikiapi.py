"""
Using this module, one can search wikipedia and get content.
"""

import requests
import json
import bs4

class WikiApi:
    """
    Class for setting up API. Contains methods for loading suggestions.
    """
    url = 'http://en.wikipedia.org/w/api.php'
    headers = {
        'Content-Type': 'application/json'
    }

    def load_suggestions(self, search_term):
        params = {
            'action': 'opensearch',
            'search': search_term,
            'format': 'json'
        }
        response = requests.get(url=self.url, headers=self.headers, params=params)
        suggestions = json.loads(response.text)
        results = {}
        for title, link in zip(suggestions[1], suggestions[3]):
            results[title] = link
        return results

    def get_article(self, url):
        response = requests.get(url=url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        f = open('result.html', 'wb')
        f.write(soup.encode('utf-8'))
        f.close()



wiki = WikiApi()
results = wiki.load_suggestions('Apple')
wiki.get_article(results['Apple'])

