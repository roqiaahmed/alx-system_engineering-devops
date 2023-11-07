#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, print None.
    """
    try:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {"User-Agent": "My-User-Agent"}
        res = requests.get(url, headers=headers, params={"limit": 10})
        data = res.json()
        titles = data["data"]["children"]
        for title in titles:
            print(title["data"]["title"])
        if data["error"] == 404:
            print(None)
            return None
        return titles
    except Exception as e:
        return None
