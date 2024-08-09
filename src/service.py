import requests


database = {1: "Alice", 2: "Bob", 3: "Charlie"}


def get_user_from_db(user_id):
    return database.get(user_id)


def get_posts():
    response = requests.get(r"https://jsonplaceholder.typicode.com/posts")
    if response.status_code != 200:
        raise requests.HTTPError
    return response.json()
