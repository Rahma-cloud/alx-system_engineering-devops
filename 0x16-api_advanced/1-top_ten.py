#!/usr/bin/python3
"""Task 1"""

import requests
import sys


def top_ten(subreddit):
    """return the titles of ten hot posts"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'my-app/0.0.1'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                title = post['data']['title']
                print(title)
        else:
            print(None)
    except requests.exceptions.HTTPError as e:
        print(None)


if __name__ == "__main__":
    top_ten(sys.argv[1])
