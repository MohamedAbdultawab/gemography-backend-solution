import requests
from datetime import date, timedelta
from collections import Counter

def get_repos():
    response = requests.get(f"https://api.github.com/search/repositories?q=created:>{date.today() - timedelta(days=30)}&sort=stars&order=desc")
    content = response.json()
    if content['incomplete_results']:
        return []
    return content['items'][:100]


def get_languages(repos):
    pass