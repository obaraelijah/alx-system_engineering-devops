#!/usr/bin/python3

"""This module contains a function that queries the Reddit API
and prints the titles of the first 10 hot posts for a given subreddit
"""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed`
    """
    url = 'https://reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    limit = {'limit': 10}

    response = requests.get(url, headers=headers, params=limit)

    if not response:
        print(None)
    else:
        posts = response.json().get('data').get('children')

        for post in posts:
            title = post.get('data').get('title')
            print(title)
