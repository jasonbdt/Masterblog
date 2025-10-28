import json
from typing import Any, Optional


def get_blog_posts() -> Optional[Any]:
    try:
        with open("data/posts.json", "r") as file_obj:
            return json.load(file_obj)
    except FileNotFoundError:
        print("Error: File not found")


def save_posts(posts: list[dict]):
    try:
        with open("data/posts.json", "w") as file_obj:
            file_obj.write(json.dumps(posts))
            print("Posts saved to file storage")
    except FileNotFoundError:
        print("Error: File not found")
