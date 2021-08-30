from warnings import simplefilter
from dotenv import load_dotenv
import os
import praw
import tkinter as tk
from tkinter import *
import webbrowser

MAX_POSTS = 20
load_dotenv('.env')


class Application(tk.Frame):

    def __init__(self, posts, master=None):
        # initialize Application window along with a list of posts (instances of the Post class corresponding to hot posts on subreddit)
        super().__init__(master)
        self.master = master
        self.posts = posts
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # create the labels & buttons to display top hot posts & visit article
        # TODO: simplify so user just needs to click the label to visit the site
        labels = []
        buttons = [NONE] * MAX_POSTS
        for i in range(MAX_POSTS):
            label = tk.Label(self, text=self.posts[i].title + "\nwww.reddit.com" + self.posts[i].permalink)
            label.grid(row=i, column=0, sticky=W, pady=1)
            labels.append(label)
            buttons[i] = tk.Button(self, text="link")
            buttons[i].grid(row=i, column=1, sticky=E, pady=1, padx=2)
        
        # TODO: this needs to be a loop for best-practice
        # update the link for each button to open the correct article
        buttons[0].configure(command = lambda: webbrowser.open(self.posts[0].url))
        buttons[1].configure(command = lambda: webbrowser.open(self.posts[1].url))
        buttons[2].configure(command = lambda: webbrowser.open(self.posts[2].url))
        buttons[3].configure(command = lambda: webbrowser.open(self.posts[3].url))
        buttons[4].configure(command = lambda: webbrowser.open(self.posts[4].url))
        buttons[5].configure(command = lambda: webbrowser.open(self.posts[5].url))
        buttons[6].configure(command = lambda: webbrowser.open(self.posts[6].url))
        buttons[7].configure(command = lambda: webbrowser.open(self.posts[7].url))
        buttons[8].configure(command = lambda: webbrowser.open(self.posts[8].url))
        buttons[9].configure(command = lambda: webbrowser.open(self.posts[9].url))
        buttons[10].configure(command = lambda: webbrowser.open(self.posts[10].url))
        buttons[11].configure(command = lambda: webbrowser.open(self.posts[11].url))
        buttons[12].configure(command = lambda: webbrowser.open(self.posts[12].url))
        buttons[13].configure(command = lambda: webbrowser.open(self.posts[13].url))
        buttons[14].configure(command = lambda: webbrowser.open(self.posts[14].url))
        buttons[15].configure(command = lambda: webbrowser.open(self.posts[15].url))
        buttons[16].configure(command = lambda: webbrowser.open(self.posts[16].url))
        buttons[17].configure(command = lambda: webbrowser.open(self.posts[17].url))
        buttons[18].configure(command = lambda: webbrowser.open(self.posts[18].url))
        buttons[19].configure(command = lambda: webbrowser.open(self.posts[19].url))


def get_reddit():
    # get the credentials of the reddit user & bot
    reddit = praw.Reddit(
        user_agent = "comment-gathering script by u/DirkIsTheGOAT41",
        username = os.getenv('BOT_USERNAME'),
        password = os.getenv('BOT_PASSWORD'),
        client_id = os.getenv('BOT_CLIENT_ID'),
        client_secret = os.getenv('BOT_CLIENT_SECRET'),
    )
    return reddit

def get_hot_posts(subreddit):
    # get the top x posts from a given subreddit (set to 20 by default)
    posts = []
    i = 0
    for submission in subreddit.hot(limit=MAX_POSTS):
        # traverse through the top x posts in r/news, store them in an instance of Post, & display basic info on each
        posts.append(Post(submission.title, submission.permalink, submission.selftext, submission.url, submission.score))
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
    # get the reddit credentials, then the subreddit to be scrapped, then get the posts & send them to the application window
    reddit = get_reddit()
    subreddit = reddit.subreddit("news")
    posts = get_hot_posts(subreddit)
    print_posts(posts)

    # setup the application window & main loop
    root = tk.Tk()
    app = Application(posts, master=root)
    app.mainloop()

main()
