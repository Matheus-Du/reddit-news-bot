from warnings import simplefilter
from dotenv import load_dotenv
import os
import praw
import tkinter as tk
from tkinter import Label, Listbox, ttk, font

MAX_POSTS = 20
load_dotenv('.env')


class Application(tk.Frame):
    def __init__(self, posts, master=None):
        super().__init__(master)
        self.master = master
        self.posts = posts
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.labels = []
        for i in range(MAX_POSTS):
            self.label = tk.Label(self, text=self.posts[i].title + "\n" + self.posts[i].permalink)
            self.label.pack(side="top", anchor='w')
            self.labels.append(self.label)
            



def get_reddit():
    reddit = praw.Reddit(
        user_agent = "comment-gathering script by u/DirkIsTheGOAT41",
        username = os.getenv('BOT_USERNAME'),
        password = os.getenv('BOT_PASSWORD'),
        client_id = os.getenv('BOT_CLIENT_ID'),
        client_secret = os.getenv('BOT_CLIENT_SECRET'),
    )
    return reddit

def get_hot_posts(subreddit):
    posts = [None] * MAX_POSTS
    i = 0
    for submission in subreddit.hot(limit=MAX_POSTS):
        # traverse through the top x posts in r/news, store them in an instance of Post, & display basic info on each
        posts[i] = Post(submission.title, submission.permalink, submission.selftext, submission.url, submission.score)
        i += 1
    return posts

def print_posts(posts):
    # print posts along with info (subtext/permalink)
    for post in posts:
        print(post.title)
        if not post.selftext:
            print("\t{}\n".format(post.url))
        else:
            print("\t{}\n".format(post.selftext))

class Post:
    # Post class creates an instance of a post on the subreddit along with some important info (i.e. subtext)
    def __init__(self, title, permalink, selftext, url, score):
        self.title = title
        self.permalink = permalink
        self.selftext = selftext
        self.url = url
        self.score = score
        
def main():
    reddit = get_reddit()
    subreddit = reddit.subreddit("news")
    posts = get_hot_posts(subreddit)
    print_posts(posts)

    root = tk.Tk()
    app = Application(posts, master=root)
    app.mainloop()

main()
