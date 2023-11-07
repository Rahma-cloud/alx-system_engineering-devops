#!/usr/bin/python3
"""Task 0"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subcribers"""
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'my-app/0.0.1'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return 0
        data = response.json()
        return data['data']['subscribers']
    except Exception as e:
        print(f"Error: {e}")
        return 0
