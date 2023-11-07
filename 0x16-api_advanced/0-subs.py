#!/usr/bin/python3
"""Task 0"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subcribers"""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return 0
        data = response.json()
        return data['data']['subscribers']
    except Exception as e:
        print(f"Error: {e}")
        return 0
