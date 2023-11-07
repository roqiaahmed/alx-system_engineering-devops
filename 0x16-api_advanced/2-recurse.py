#!/usr/bin/python3
"""
2-recurse
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "My Reddit Recursive Bot"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]

        if children:
            for child in children:
                title = child["data"]["title"]
                hot_list.append(title)

            after = data["data"]["after"]
            if after:
                return recurse(subreddit, hot_list=hot_list)
            else:
                return hot_list
        else:
            return hot_list
    else:
        return None
