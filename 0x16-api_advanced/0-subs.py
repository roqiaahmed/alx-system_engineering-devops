#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {"User-Agent": "My-User-Agent"}
        res = requests.get(url, headers=headers)
        data = res.json()
        sub = data["data"]["subscribers"]
        return sub
    except Exception as e:
        return 0
