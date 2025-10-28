from typing import Optional, Union

from flask import Flask, redirect, request, render_template, url_for, Response

import utils

app = Flask(__name__)


@app.route('/')
def index() -> Optional[str]:
    blog_posts = utils.get_blog_posts()

    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add() -> Union[str, Response]:
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        content = request.form.get('content')

        blog_posts = utils.get_blog_posts()
        post_exist = list(
            filter(lambda post: post['title'] == title, blog_posts)
        )

        if post_exist:
            print("Error") # TODO: Return error that post already exists
        else:
            new_blog_post = {
                "id": blog_posts[-1]['id'] + 1,
                "title": title,
                "author": author,
                "content": content
            }

            blog_posts.append(new_blog_post)
            utils.save_posts(blog_posts)

            return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/delete/<int:post_id>')
def delete(post_id: int) -> Union[str, Response]:
    blog_posts: list[dict] = utils.get_blog_posts()
    post_to_delete = list(
        filter(lambda post: post['id'] == post_id, blog_posts)
    )

    if post_to_delete:
        blog_posts.remove(post_to_delete[0])
        print(f'Blog post with ID {post_id} deleted.')
        utils.save_posts(blog_posts)

        return redirect(url_for('index'))

    return render_template(
        'index.html',
        posts=blog_posts,
        form_error=f"No post found with ID {post_id}")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
