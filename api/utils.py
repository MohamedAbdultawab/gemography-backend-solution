import requests
from datetime import date, timedelta
from collections import OrderedDict, defaultdict


def get_repos():
    """Retrieve first 100 trending repo on Github in the last 30 days.

    Returns:
        List[dict]: List of dictionary objects, each represent a repo.
    """
    response = requests.get(
        f"https://api.github.com/search/repositories?q=created:>{date.today() - timedelta(days=30)}&sort=stars&order=desc&&per_page=100"
    )
    content = response.json()
    if content["incomplete_results"]:
        return []
    return content["items"][:100]


def create_languages_dict(repos):
    """Given list of repos, each represented with a dictionary.

    Args:
        repos (List[dict]): List of dictionary objects, each represent a repo.

    Returns:
        dict: Each key represent a language, and its value contains language related info\
            `repos_count` and `repos`.
    """
    languages = defaultdict(lambda: {"repos_count": 0, "repos": list()})

    for repo in repos:
        language = languages[repo["language"]]
        language["repos_count"] += 1
        language["repos"].append(repo["html_url"])

    return OrderedDict(
        (k, v)
        for k, v in sorted(
            languages.items(), key=lambda item: item[1]["repos_count"], reverse=True
        )
    )


def get_languages():
    """A utility to call helper methods to get repos and extract language information.

    Returns:
        dict: Each key represent a language, and its value contains language related info\
            `repos_count` and `repos`.
    """
    return create_languages_dict(get_repos())
