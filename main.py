from flask import Flask
import praw
import urllib.request as url

reddit = praw.Reddit(
    client_id="v6_Vk41Bij9p8obun6BvkQ",
    client_secret="Ec8TxEaAaY5SYMf-TP8BdF6yyYzSpQ",
    user_agent="my user agent",
)

def getDaStuff(sub):
  x = reddit.subreddit(sub).random()
  if (x.url).endswith('jpg') or (x.url).endswith('png') or (x.url).endswith('jpeg'):
    return x.url

print(getDaStuff('cats'))

app = Flask(__name__)

@app.route('/')
def ret():
  return "<p>die</p>"

@app.route('/r/<sub>')
def index(sub):
  return getDaStuff(sub)

app.run(port=81,host= '0.0.0.0')