# Masterblog

This repository is for learning purposes only. The goal of the repository is to
build our very own Blog Application using Python + Flask.

## Setup

Clone this repository and run `pip install -r requirements.txt` to install
the required packages. We recommend to use `.venv`, please check how to
setup your virtual environment for python development.

After package installation, you can run:

```bash
python app.py
```

The application provides a webserver that listens
on port 5000 (visit: [localhost:5000](http://localhost:5000/))
## Packages
- Python 3.13
- Flask 3.1

## Features
- Blog posts are stored in a JSON file
- Displays each blog post on index page
- User is able to create new posts with "Add Post"
- User can delete posts that aren't longer needed with "Delete Post"
- User can update posts
- User can like posts
