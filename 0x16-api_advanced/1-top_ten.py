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

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}
    req = requests.get(url, headers=headers, params={"limit": 10})
    if req.status_code == 200:
        data = req.json()
        titles = data["data"]["children"]
        for title in titles:
            print(title["data"]["title"])
    else:
        print("None")
