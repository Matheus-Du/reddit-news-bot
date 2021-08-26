from dotenv import load_dotenv
import os
import praw
MAX_POSTS = 20

load_dotenv('.env')

reddit = praw.Reddit(
    user_agent = "comment-gathering script by u/DirkIsTheGOAT41",
    username = os.getenv('BOT_USERNAME'),
    password = os.getenv('BOT_PASSWORD'),
    client_id = os.getenv('BOT_CLIENT_ID'),
    client_secret = os.getenv('BOT_CLIENT_SECRET'),
)

subreddit = reddit.subreddit("news")

class Post:
    def __init__(self, title, permalink, url, score):
        self.title = title
        self.permalink = permalink
        self.url = url
        self.score = score

posts = [None] * MAX_POSTS
i = 0
for submission in subreddit.hot(limit=MAX_POSTS):
    posts[i] = Post(submission.title, submission.permalink, submission.url, submission.score)
    print("{} \n\t{} \n".format(posts[i].title, posts[i].url))
    i += 1