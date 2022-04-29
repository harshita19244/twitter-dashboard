from ast import keyword
import imp
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from dominate.tags import img
import numpy as np
import pandas as pd
from os import path
from PIL import Image
import re
from sqlalchemy import null
from torch import real
import tweepy
from tweepy import OAuthHandler
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib
import matplotlib.pyplot as plt
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
matplotlib.use('Agg')
import sqlite3
import time
import asyncio
import threading
import categorical_wordcloud
import geoheatmap
import input_tweet
import query_users
import likesuser
import bargraph
import json
import plotly
import plotly.express as px
from models.hsol import caller as cl1
from models.fakeddit_2 import caller as cl2
from models.fakeddit_6 import caller as cl3
from models.implicit_3 import caller as cl4
from models.implicit_6 import caller as cl5
import logging
import preprocessor as p

consumer_key = "YiqFm45PnIiGtmFuGYEIb0dQj"
consumer_secret = "zD0CIfO4JCanUqeyJbQ4r3Zw4mCxFTyBYAePnTOjkMrGwz0QLl"
access_token = "899977011774369795-VDedKBd2KOO0xtmOJZWLqJHognDLZOo"
access_token_secret = "Nd83xEIqrxFpTj6ThCQ9FaRBzA2NLyjenFcGfIMuaFqFM"

df = pd.DataFrame(columns=["Date","User","IsVerified","Tweet","Likes","RT",'User_location'])
tags = ['True', 'Satire', 'Misleading', 'Manipulated', 'False', 'Impostor']
app = Flask(__name__)

from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)
from sassutils.wsgi import SassMiddleware
app.wsgi_app = SassMiddleware(app.wsgi_app, {
    'main': ('static/sass', 'static/styles', '/static/styles')
})

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///twitter.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Twitter(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    Date = db.Column(db.DateTime,  nullable=False, default = datetime.utcnow)
    User = db.Column(db.String(80),nullable=False)
    IsVerified = db.Column(db.Boolean,default=False)
    Tweet = db.Column(db.String(150),nullable = False)
    Likes = db.Column(db.Integer,nullable = False)
    RT = db.Column(db.Integer,nullable =False)
    User_location = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f"{self.user}-{self.tweet}"


def func(Topic,Count):

    # Use the above credentials to authenticate the API.
    i = 0
    auth = tweepy.OAuthHandler( consumer_key , consumer_secret )
    auth.set_access_token( access_token , access_token_secret )
    api = tweepy.API(auth)
    for tweet in tweepy.Cursor(api.search_tweets, q=Topic, count=5000, lang="en", exclude='retweets').items(5000):
            #time.sleep(0.1)
            #my_bar.progress(i)
            df.loc[i,"Date"] = tweet.created_at
            df.loc[i,"User"] = tweet.user.name
            df.loc[i,"IsVerified"] = tweet.user.verified
            df.loc[i,"Tweet"] = tweet.text
            df.loc[i,"Likes"] = tweet.favorite_count
            df.loc[i,"RT"] = tweet.retweet_count
            df.loc[i,"User_location"] = tweet.user.location
            df.loc[i,"Coordinates"] = tweet.coordinates
            df.loc[i,"Places"] = tweet.place
            #df.to_csv("TweetDataset.csv",index=False)
            #df.to_excel('{}.xlsx'.format("TweetDataset"),index=False)   ## Save as Excel
            i = i+1
            if i > Count:
                break
            else:
                pass
    print(df["User_location"])
    df.to_csv("TweetDataset.csv",index=False)


def realTimeTweets():
    auth = tweepy.OAuthHandler( consumer_key , consumer_secret )
    auth.set_access_token( access_token , access_token_secret )
    api = tweepy.API(auth)
    class Listener(tweepy.Stream):

        tweet_str = ""

        def on_status(self, status):
            
            if not status.truncated:

                tweet_1 = Twitter(Date = status.created_at,User = status.user.name,IsVerified = status.user.verified,Tweet = status.text,Likes = status.favorite_count
                ,RT = status.retweet_count,User_location = status.user.location)
                db.session.add(tweet_1)
                db.session.commit()

            else:

                tweet_1 = Twitter(Date = status.created_at,User = status.user.name,IsVerified = status.user.verified,Tweet = status.extended_tweet['full_text'],Likes = status.favorite_count
                ,RT = status.retweet_count,User_location = status.user.location)
                db.session.add(tweet_1)
                db.session.commit()
            time.sleep(30)
            df_5 = dbtodf()
            print(df_5)
            print(df_5.columns)
    
    stream_tweet = Listener(consumer_key, consumer_secret,access_token,access_token_secret)

    keywords = ["fake","elon musk","russia","ukraine","hate"]
    stream_tweet.filter(track=keywords)


def dbtodf():
    #This function takes the twitter.db file and converts all the data inside it to a dataframe
    #This is done as all the functions take Dataframe as input
    #This Will return the dataframe of the twitter.db when it is called

    cnx = sqlite3.connect('twitter.db')

    df = pd.read_sql_query("SELECT * FROM 'twitter'", cnx)

    return df


@app.route('/home',methods = ['GET'])
def get_home():
    threading.Thread(target=realTimeTweets).start()
    # return render_template('primary.html')
    return render_template('home.html')
    
@app.route('/wordcloud')
def view_wordcloud():
    df = dbtodf()
    names, urls = categorical_wordcloud.create_wordcloud(df)
    return render_template('index.html', url = urls, name = names)

@app.route('/bargraph')
def view_bargraph():
    df = dbtodf()
    graphJSON = bargraph.plot_bargraph(df)
    return render_template('bargraph2.html', graphJSON=graphJSON)

@app.route('/geoheatmap')
def view_geoheatmap(): 
    graphJSON, urls, names = geoheatmap.create_geoheatmap()
    return render_template('geoheatmap.html', url = urls, name = names, graphJSON=graphJSON)

@app.route('/dispersionnetwork',methods=['GET', 'POST'])
def view_dispersion():
    return render_template('network.html')

@app.route("/query5")
def plot_users():
    df = dbtodf()
    graphJSON = query_users.user_plots(df, app)
    return render_template('query10.html', graphJSON=graphJSON)
@app.route("/likes5")
def plot_users_likes():
    df = dbtodf()
    graphJSON_likes = likesuser.user_plots(df, app)
    return render_template('likes5.html', graphJSON_likes=graphJSON_likes)

@app.route('/inputtext', methods=['GET', 'POST'])
def classify_inputtext():
    if request.method == 'POST':
        text = request.form['text']
        # processed_text = text.upper()
        processed_text = p.clean(text)
        predictions = input_tweet.classify_input_tweet(processed_text)

        # hsol

        if predictions[0] == 0:
                predictions[0] = 'hate'
        elif predictions[0] == 1:
                predictions[0] = 'offensive'
        elif predictions[0] == 2:
                predictions[0] = 'none'

        # fakeddit

        if predictions[1] == 0:
                predictions[1] = 'true'
        elif predictions[1] == 1:
                predictions[1] = 'false'

        if predictions[2] == 0:
                predictions[2] = 'true'
        elif predictions[2] == 1:
                predictions[2] = 'satire'
        elif predictions[2] == 2:
                predictions[2] = 'misleading'
        elif predictions[2] == 3:
                predictions[2] = 'false'
        elif predictions[2] == 4:
                predictions[2] = 'imposter'
        elif predictions[2] == 5:
                predictions[2] = 'manipulated'

        # implicit

        if predictions[3] == 0:
                predictions[3] = 'explicit hate'
        elif predictions[3] == 1:
                predictions[3] = 'implicit hate'
        elif predictions[3] == 2:
                predictions[3] = 'not hate'

        if predictions[4] == 0:
                predictions[4] = 'incitement'
        elif predictions[4] == 1:
                predictions[4] = 'inferiority'
        elif predictions[4] == 2:
                predictions[4] = 'irony'
        elif predictions[4] == 3:
                predictions[4] = 'stereotypical'
        elif predictions[4] == 4:
                predictions[4] = 'threatening'
        elif predictions[4] == 5:
                predictions[4] = 'white grievance'
        return render_template('inputtext.html', tweet = processed_text, names = predictions)
    else:
        predictions = ['', '', '', '', '']
        text = 'Please enter text to classify'
        return render_template('inputtext.html', tweet = text, names = predictions)

@app.route('/contact')
def get_contact():
    return render_template('contactUs.html')

@app.route('/background')
def get_background():
    return render_template('background.html')

@app.after_request
def add_header(response):
	"""
		Add headers to both force latest IE rendering engine or Chrome Frame,
		and also to cache the rendered page for 10 minutes.
		"""
	response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
	response.headers['Cache-Control'] = 'public, max-age=0'
	return response

if __name__ == '__main__':
    app.run(debug=True)
