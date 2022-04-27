
import logging

from ast import keyword
from email.policy import default

from flask import Flask, render_template
# from aioflask import Flask, render_template
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
import subprocess
from models.hsol import caller as cl1
from models.fakeddit_2 import caller as cl2
from models.fakeddit_6 import caller as cl3
from models.implicit_3 import caller as cl4
from models.implicit_6 import caller as cl5
import preprocessor as p
matplotlib.use('Agg')
import sqlite3
import time
import asyncio
import threading
import categorical_wordcloud
import geoheatmap
import input_tweet
import json
import plotly
import plotly.express as px

consumer_key = "YiqFm45PnIiGtmFuGYEIb0dQj"
consumer_secret = "zD0CIfO4JCanUqeyJbQ4r3Zw4mCxFTyBYAePnTOjkMrGwz0QLl"
access_token = "899977011774369795-VDedKBd2KOO0xtmOJZWLqJHognDLZOo"
access_token_secret = "Nd83xEIqrxFpTj6ThCQ9FaRBzA2NLyjenFcGfIMuaFqFM"

df = pd.DataFrame(columns=["Date","User","IsVerified","Tweet","Likes","RT",'User_location'])
labels= [0,0,0,0,0,0]
tags = ['True', 'Satire', 'Misleading', 'Manipulated', 'False', 'Impostor']
app = Flask(__name__)

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


# def func(Topic,Count):

#     # Use the above credentials to authenticate the API.
#     i = 0
#     auth = tweepy.OAuthHandler( consumer_key , consumer_secret )
#     auth.set_access_token( access_token , access_token_secret )
#     api = tweepy.API(auth)
#     for tweet in tweepy.Cursor(api.search_tweets, q=Topic, count=5000, lang="en", exclude='retweets').items(5000):
#             #time.sleep(0.1)
#             #my_bar.progress(i)
#             df.loc[i,"Date"] = tweet.created_at
#             df.loc[i,"User"] = tweet.user.name
#             df.loc[i,"IsVerified"] = tweet.user.verified
#             df.loc[i,"Tweet"] = tweet.text
#             df.loc[i,"Likes"] = tweet.favorite_count
#             df.loc[i,"RT"] = tweet.retweet_count
#             df.loc[i,"User_location"] = tweet.user.location
#             df.loc[i,"Coordinates"] = tweet.coordinates
#             df.loc[i,"Places"] = tweet.place
#             #df.to_csv("TweetDataset.csv",index=False)
#             #df.to_excel('{}.xlsx'.format("TweetDataset"),index=False)   ## Save as Excel
#             i = i+1
#             if i > Count:
#                 break
#             else:
#                 pass
#     print(df["User_location"])
#     df.to_csv("TweetDataset.csv",index=False)


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

            # time.sleep(5)
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
    return render_template('primary.html')
    
@app.route('/wordcloud')
def view_wordcloud():
    df = dbtodf()
    names, urls = categorical_wordcloud.create_wordcloud(df)
    return render_template('index.html', url = urls, name = names)


@app.route('/bargraph')
def view_bargraph():
    df = dbtodf()
    i = 0
    tweets = df['Tweet']
    for i in range(len(labels)):
        labels[i] += np.random.randint(0,6)
        i = i + 1 
    x_axis= ['Grievance', 'Incitement', 'Threats', 'Irony', 'Stereotypes', 'Inferiority']
    plt.bar(x_axis, labels,color=['cyan','red','purple','green', 'blue', 'black'])
    plt.savefig('./static/images/bar_plot.png')
    return render_template('index.html', name = 'bar_plot', url = './static/images/bar_plot.png')


@app.route('/geoheatmap')
def view_geoheatmap():
    # realTimeTweets()
    df = dbtodf()
    graphJSON, urls, names = geoheatmap.create_geoheatmap(df)
    return render_template('geoheatmap.html', url = urls, name = names, graphJSON=graphJSON)


@app.route('/dispersionnetwork',methods=['GET', 'POST'])
def view_dispersion():
    return render_template('network.html')

@app.route("/query5")
def plot_users():
    df = dbtodf()
    data = cl3(df)
    count=[0,0,0,0,0,0]
    for i in range(len(count)):
        count[i]=len(data.loc[data['Category']==i])


    #data2=cl3(df)
    for i in count:
        app.logger.info("manasvi")
        app.logger.info(i)
    #app.logger.info(data2.loc[0])
    

    get_0_data=data.loc[data['Category']==0]
    sorted_0=get_0_data.groupby("User").size()
    sorted_0=sorted_0.sort_values(ascending=False)
    sorted_0=sorted_0[0:5]
    fig = px.bar(x=sorted_0.index, y=sorted_0)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# tweets")
    fig.update_layout(showlegend=False)
    #fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON0 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    '''
    get_1_data=data.loc[data['Category']==1]
    sorted_1=get_1_data.groupby("User").size()
    sorted_1=sorted_1.sort_values(ascending=False)
    sorted_1=sorted_1[0:5]
    fig = px.bar(x=sorted_1.index, y=sorted_1)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# tweets")
    fig.update_layout(showlegend=False)
    #fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    '''
    get_2_data=data.loc[data['Category']==2]
    sorted_2=get_2_data.groupby("User").size()
    sorted_2=sorted_2.sort_values(ascending=False)
    sorted_2=sorted_2[0:5]
    fig = px.bar(x=sorted_2.index, y=sorted_2)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# tweets")
    fig.update_layout(showlegend=False)
    #fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    get_3_data=data.loc[data['Category']==3]
    sorted_3=get_3_data.groupby("User").size()
    sorted_3=sorted_3.sort_values(ascending=False)
    sorted_3=sorted_3[0:5]
    fig = px.bar(x=sorted_3.index, y=sorted_3)
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# tweets")
    fig.update_layout(showlegend=False)
    #fig.update_layout(yaxis={'visible': False, 'showticklabels': False})
    fig.update_layout(xaxis={'showticklabels': False})    
    graphJSON3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    get_4_data=data.loc[data['Category']==4]
    sorted_4=get_4_data.groupby("User").size()
    sorted_4=sorted_4.sort_values(ascending=False)
    sorted_4=sorted_4[0:5]
    app.logger.info(sorted_4.index)
    app.logger.info(len(sorted_4[0:5]))
    app.logger.info('before plotting fig')
    fig = px.bar(x=sorted_4.index, y=sorted_4)
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# tweets")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    get_5_data=data.loc[data['Category']==5]
    sorted_5=get_5_data.groupby("User").size()
    sorted_5=sorted_5.sort_values(ascending=False)
    sorted_5=sorted_5[0:5]
    app.logger.info(sorted_5.index)
    app.logger.info(len(sorted_5[0:5]))
    app.logger.info('before plotting fig')
    fig = px.bar(x=sorted_5.index, y=sorted_5)
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# tweets")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON5 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    sorted_likes_count_0=get_0_data.drop_duplicates("User")
    sorted_likes_count_0=sorted_likes_count_0.sort_values("Likes",ascending=False)
    sorted_likes_count_0=sorted_likes_count_0[0:5]
    fig = px.bar(x=sorted_likes_count_0["User"], y=sorted_likes_count_0["Likes"])
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# Likes")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_likes_0 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    '''
    sorted_likes_count_1=get_1_data.drop_duplicates("User")
    sorted_likes_count_1=sorted_likes_count_1.sort_values("Likes",ascending=False)
    sorted_likes_count_1=sorted_likes_count_1[1:5]
    app.logger.info("sorted length")
    app.logger.info(len(sorted_likes_count_1))
    fig = px.bar(x=sorted_likes_count_1["User"], y=sorted_likes_count_1["Likes"])
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# Likes")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_likes_1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    '''
    sorted_likes_count_2=get_2_data.drop_duplicates("User")
    sorted_likes_count_2=sorted_likes_count_2.sort_values("Likes",ascending=False)
    sorted_likes_count_2=sorted_likes_count_2[2:5]
    fig = px.bar(x=sorted_likes_count_2["User"], y=sorted_likes_count_2["Likes"])
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# Likes")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_likes_2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    sorted_likes_count_3=get_3_data.drop_duplicates("User")
    sorted_likes_count_3=sorted_likes_count_3.sort_values("Likes",ascending=False)
    sorted_likes_count_3=sorted_likes_count_3[3:5]
    fig = px.bar(x=sorted_likes_count_3["User"], y=sorted_likes_count_3["Likes"])
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# Likes")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_likes_3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    sorted_likes_count_4=get_4_data.drop_duplicates("User")
    sorted_likes_count_4=sorted_likes_count_4.sort_values("Likes",ascending=False)
    sorted_likes_count_4=sorted_likes_count_4[4:5]
    fig = px.bar(x=sorted_likes_count_4["User"], y=sorted_likes_count_4["Likes"])
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# Likes")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_likes_4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    '''
    sorted_likes_count_5=get_5_data.drop_duplicates("User")
    sorted_likes_count_5=sorted_likes_count_5.sort_values("Likes",ascending=False)
    sorted_likes_count_5=sorted_likes_count_5[5:5]
    fig = px.bar(x=sorted_likes_count_5["User"], y=sorted_likes_count_5["Likes"])
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# Likes")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_likes_5 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    '''

    return render_template('query10.html', graphJSON0=graphJSON0, graphJSON1=graphJSON0, graphJSON2=graphJSON2, graphJSON3=graphJSON3, graphJSON4=graphJSON4,graphJSON5=graphJSON5,graphJSON_likes_0=graphJSON_likes_0,graphJSON_likes_1=graphJSON_likes_0,graphJSON_likes_2=graphJSON_likes_2,graphJSON_likes_3=graphJSON_likes_3,graphJSON_likes_4=graphJSON_likes_4,graphJSON_likes_5=graphJSON_likes_4)


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
