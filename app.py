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
    blog_posts = utils.get_blog_posts()
    post = utils.fetch_post_by_id(post_id)

    if post:
        blog_posts.remove(post)
        print(f'Blog post with ID {post_id} deleted.')
        utils.save_posts(blog_posts)

        return redirect(url_for('index'))

    return render_template(
        'index.html',
        posts=blog_posts,
        form_error=f"No post found with ID {post_id}")


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id: int) -> Union[str, tuple[str, int], Response]:
    post = utils.fetch_post_by_id(post_id)
    blog_posts = utils.get_blog_posts()

    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        post_to_update = blog_posts.index(post)
        blog_posts[post_to_update].update({
            "title": request.form.get('title', post['title']),
            "author": request.form.get('author', post['author']),
            "content": request.form.get('content', post['content'])
        })
        utils.save_posts(blog_posts)

        return redirect(url_for('index'))

    return render_template('update.html', post=post)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
