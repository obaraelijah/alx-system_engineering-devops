#!/usr/bin/python3
"""fetching json data from an api"""

import csv
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    user_dict = requests.get(user_url).json()
    user_name = user_dict.get("username")
    user_todo = requests.get("{}/todos".format(user_url))
    user_todo = user_todo.json()
    file_name = user_id + ".json"
    my_dict = {}

    my_dict[user_id] = []

    for item in user_todo:
        inner_dict = {}
        inner_dict["task"] = item.get("title")
        inner_dict["completed"] = item.get("completed")
        inner_dict["username"] = user_name
        my_dict.get(user_id).append(inner_dict)

    with open(file_name, 'w') as f:
        json.dump(my_dict, f)
