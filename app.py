from typing import Optional

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index() -> Optional[str]:
    try:
        with open("data/posts.json", "r") as file_obj:
            blog_posts = file_obj.read()
    except FileNotFoundError:
        print("No posts")
    else:
        return render_template('index.html', posts=blog_posts)

    return None


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
