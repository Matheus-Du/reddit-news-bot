from dotenv import load_dotenv
import os
import praw

load_dotenv('.env')

reddit = praw.Reddit(
    user_agent = "comment-gathering script by u/DirkIsTheGOAT41",
    username = os.getenv('BOT_USERNAME'),
    password = os.getenv('BOT_PASSWORD'),
    client_id = os.getenv('BOT_CLIENT_ID'),
    client_secret = os.getenv('BOT_CLIENT_SECRET'),
)

subreddit = reddit.subreddit("news")

for submission in subreddit.hot(limit=20):
    print("{} \n\t{} \n".format(submission.title, submission.url))