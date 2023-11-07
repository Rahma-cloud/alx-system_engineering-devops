#!/usr/bin/python3
"""Task 2"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """return the titles recursively"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}'
    headers = {'User-Agent': 'my-app/0.0.1'}
    params = {'after': after} if after else {}

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
        )
        response.raise_for_status()
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            if not posts:
                return hot_list
        else:
            titles = [post['data']['title'] for post in posts]
            hot_list.extend(titles)
            after = data['data']['after']
            return recurse(subreddit, hot_list, after)

    except requests.exceptions.HTTPError as e:
        return None
