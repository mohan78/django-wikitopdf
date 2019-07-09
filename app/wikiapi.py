"""
Using this module, one can search wikipedia and get content.
"""

import requests
import json
import bs4
import wikipedia

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
        page = wikipedia.page(url)
        return page

