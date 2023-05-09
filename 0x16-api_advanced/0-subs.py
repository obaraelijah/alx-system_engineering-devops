#!/usr/bin/python3

"""This module contains a function that queries the Reddit API
and returns the number of subscribers for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for an existing
    subreddit
    Return:
        number of subscribers (int)
    """
    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    if not response:
        return 0
    else:
        data = response.json().get('data')
        return data.get('subscribers')
