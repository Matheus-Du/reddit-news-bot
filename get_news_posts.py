from logging import root
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

    def __init__(self, subreddit, master=None):
        # initialize Application window along with a list of posts (instances of the Post class)
        super().__init__(master)
        self.master = master
        self.subreddit = subreddit
        self.posts = []
        self.pack()
        self.get_hot_posts()
        self.create_widgets()

    def get_hot_posts(self):
        # get the top x posts from a given subreddit (set to 20 by default)
        i = 0
        for submission in self.subreddit.hot(limit=MAX_POSTS):
            # traverse through the top x posts in r/news, store them in an instance of Post, & display basic info on each
            self.posts.append(Post(submission.title, submission.permalink, submission.selftext, submission.url, submission.score))
            i += 1

    def create_widgets(self):
        # create the labels & buttons to display top hot posts & visit article
        # TODO: simplify so user just needs to click the label to visit the site
        labels = []
        for i in range(MAX_POSTS):
            label = tk.Label(self, text=self.posts[i].title + "\nwww.reddit.com" + self.posts[i].permalink, cursor="hand2")
            label.grid(row=i, column=0, sticky=W, pady=1)
            labels.append(label)
        
        # TODO: this needs to be a loop for best-practice
        # update the link for each label to open the correct article
        labels[0].bind("<Button-1>", lambda e: webbrowser.open(self.posts[0].url))
        labels[1].bind("<Button-1>", lambda e: webbrowser.open(self.posts[1].url))
        labels[2].bind("<Button-1>", lambda e: webbrowser.open(self.posts[2].url))
        labels[3].bind("<Button-1>", lambda e: webbrowser.open(self.posts[3].url))
        labels[4].bind("<Button-1>", lambda e: webbrowser.open(self.posts[4].url))
        labels[5].bind("<Button-1>", lambda e: webbrowser.open(self.posts[5].url))
        labels[6].bind("<Button-1>", lambda e: webbrowser.open(self.posts[6].url))
        labels[7].bind("<Button-1>", lambda e: webbrowser.open(self.posts[7].url))
        labels[8].bind("<Button-1>", lambda e: webbrowser.open(self.posts[8].url))
        labels[9].bind("<Button-1>", lambda e: webbrowser.open(self.posts[9].url))
        labels[10].bind("<Button-1>", lambda e: webbrowser.open(self.posts[10].url))
        labels[11].bind("<Button-1>", lambda e: webbrowser.open(self.posts[11].url))
        labels[12].bind("<Button-1>", lambda e: webbrowser.open(self.posts[12].url))
        labels[13].bind("<Button-1>", lambda e: webbrowser.open(self.posts[13].url))
        labels[14].bind("<Button-1>", lambda e: webbrowser.open(self.posts[14].url))
        labels[15].bind("<Button-1>", lambda e: webbrowser.open(self.posts[15].url))
        labels[16].bind("<Button-1>", lambda e: webbrowser.open(self.posts[16].url))
        labels[17].bind("<Button-1>", lambda e: webbrowser.open(self.posts[17].url))
        labels[18].bind("<Button-1>", lambda e: webbrowser.open(self.posts[18].url))
        labels[19].bind("<Button-1>", lambda e: webbrowser.open(self.posts[19].url))

        # menu bar containing a refresh button
        menubar = Menu(self)
        menubar.add_command(label="Refresh", command = self.refresh)
        self.master.config(menu=menubar)

    def refresh(self):
        # destroys the current window & initializes a new one
        self.destroy()
        self.__init__(self.subreddit, self.master)


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

    # setup the application window & main loop
    root = tk.Tk()
    app = Application(subreddit, master=root)
    app.mainloop()

main()
