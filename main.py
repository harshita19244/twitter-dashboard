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
import tweepy
from tweepy import OAuthHandler
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib
import matplotlib.pyplot as plt
import geopandas as gpd
matplotlib.use('Agg')

import geoheatmap

consumer_key = "YiqFm45PnIiGtmFuGYEIb0dQj"
consumer_secret = "zD0CIfO4JCanUqeyJbQ4r3Zw4mCxFTyBYAePnTOjkMrGwz0QLl"
access_token = "899977011774369795-VDedKBd2KOO0xtmOJZWLqJHognDLZOo"
access_token_secret = "Nd83xEIqrxFpTj6ThCQ9FaRBzA2NLyjenFcGfIMuaFqFM"

df = pd.DataFrame(columns=["Date","User","IsVerified","Tweet","Likes","RT",'User_location'])
labels= [0,0,0,0,0,0]
tags = ['True', 'Satire', 'Misleading', 'Manipulated', 'False', 'Impostor']
app = Flask(__name__)

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
    
@app.route('/home',methods = ['GET'])
def get_home():
    return render_template('primary.html')
    
@app.route('/wordcloud')
def view_wordcloud():
    func('Hate',20)
    # df = pd.read_csv("./hatespeech.csv")
    text = df.Tweet[0]
    pil_img = WordCloud(collocations = False, background_color = 'white').generate(text)
    plt.imshow(pil_img, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wordcloud_plot.png')
    return render_template('index.html', name = 'wordcloud_plot', url ='/static/images/wordcloud_plot.png')

@app.route('/bargraph')
def view_bargraph():
    func('Fake',20)
    i = 0
    tweets = df['Tweet']
    for i in range(len(labels)):
        labels[i] += np.random.randint(0,6)
        i = i + 1 
    x_axis= ['Grievance', 'Incitement', 'Threats', 'Irony', 'Stereotypes', 'Inferiority']
    plt.bar(x_axis, labels,color=['cyan','red','purple','green', 'blue', 'black'])
    plt.savefig('./static/images/bar_plot.png')
    return render_template('index.html', name = 'bar_plot', url = './static/images/bar_plot.png')

import plotly
import json
import plotly.express as px
@app.route('/geoheatmap')
def view_geoheatmap():
    graphJSON, urls, names = geoheatmap.create_geoheatmap()
    return render_template('geoheatmap.html', url = urls, name = names, graphJSON=graphJSON)


@app.route("/query5")
def plot_category():
    func('Fake',20)
    data = df
    
    data['tweet_label']=0
    for i in range(len(data)):
        data['tweet_label'] = np.random.randint(0,6)
        i = i + 1 
    
    #ploting
    category = 0
    #request.form['category']
    
    get_0_data=data.loc[data['tweet_label']==0]
    sorted_0=get_0_data.groupby("User").size()
    sorted_0=sorted_0.sort_values(ascending=False)
    sorted_0=sorted_0[0:5]
    plt.bar(sorted_0.index,sorted_0,color='black')
    plt.savefig("./static/images/bar_plot_category_0.png")

    get_1_data=data.loc[data['tweet_label']==1]
    sorted_1=get_1_data.groupby("User").size()

    sorted_1=sorted_1.sort_values(ascending=False)
    sorted_1=sorted_1[0:5]
    plt.bar(sorted_1.index,sorted_1,color='black')
    plt.savefig("./static/images/bar_plot_category_1.png")
    
    get_2_data=data.loc[data['tweet_label']==2]
    sorted_2=get_2_data.groupby("User").size()


    sorted_likes_count_0=get_0_data.drop_duplicates("User")
    sorted_likes_count_0=sorted_likes_count_0.sort_values("Likes",ascending=False)
    sorted_likes_count_0=sorted_likes_count_0[0:5]
    plt.bar(sorted_likes_count_0["User"],sorted_likes_count_0["Likes"],color='black')
    plt.savefig("./static/images/bar_plot_category_0_followers.png")

    sorted_followers_count_1=get_1_data.drop_duplicates("User")
    sorted_followers_count_1=sorted_followers_count_1.sort_values("Likes",ascending=False)
    sorted_followers_count_1=sorted_followers_count_1[0:5]
    plt.bar(sorted_followers_count_1["User"].index,sorted_followers_count_1["Likes"],color='black')
    plt.savefig("./static/images/bar_plot_category_1_followers.png")    


    a,b,c,d="/static/images/bar_plot_category_0.png","/static/images/bar_plot_category_1.png","/static/images/bar_plot_category_0_followers.png","/static/images/bar_plot_category_1_followers.png"
    return render_template('query10.html',name = 'new_plot', img1=a,img2=b,img3=c,img4=d)

    return render_template('query10.html',name = 'new_plot', aa=a,bb=b,cc=c,dd=d)

@app.route('/inputtext', methods=['GET', 'POST'])
def classify_inputtext():
    if request.method == 'POST':
        text = request.form['text']
        processed_text = text.upper()
        return processed_text
    else:
        return render_template('inputtext.html')

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
