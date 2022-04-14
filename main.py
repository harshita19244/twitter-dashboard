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
matplotlib.use('Agg')

import geoheatmap
df = pd.DataFrame(columns=["Date","User","IsVerified","Tweet","Likes","RT",'User_location'])
labels= [0,0,0,0,0,0]
app = Flask(__name__)

def func(Topic,Count):
    consumer_key = "YiqFm45PnIiGtmFuGYEIb0dQj"
    consumer_secret = "zD0CIfO4JCanUqeyJbQ4r3Zw4mCxFTyBYAePnTOjkMrGwz0QLl"
    access_token = "899977011774369795-VDedKBd2KOO0xtmOJZWLqJHognDLZOo"
    access_token_secret = "Nd83xEIqrxFpTj6ThCQ9FaRBzA2NLyjenFcGfIMuaFqFM"


    # Use the above credentials to authenticate the API.
    i = 0
    auth = tweepy.OAuthHandler( consumer_key , consumer_secret )
    auth.set_access_token( access_token , access_token_secret )
    api = tweepy.API(auth)
    for tweet in tweepy.Cursor(api.search_tweets, q=Topic,count=100, lang="en",exclude='retweets').items():
            #time.sleep(0.1)
            #my_bar.progress(i)
            df.loc[i,"Date"] = tweet.created_at
            df.loc[i,"User"] = tweet.user.name
            df.loc[i,"IsVerified"] = tweet.user.verified
            df.loc[i,"Tweet"] = tweet.text
            df.loc[i,"Likes"] = tweet.favorite_count
            df.loc[i,"RT"] = tweet.retweet_count
            df.loc[i,"User_location"] = tweet.user.location
            #df.to_csv("TweetDataset.csv",index=False)
            #df.to_excel('{}.xlsx'.format("TweetDataset"),index=False)   ## Save as Excel
            i=i+1
            if i>Count:
                break
            else:
                pass
    
@app.route('/home',methods = ['GET'])
def get_home():
    return render_template('primary.html')
    
@app.route('/visualize')
def view_visualise():
    func('Hate',20)
    # df = pd.read_csv("./hatespeech.csv")
    text = df.Tweet[0]
    pil_img = WordCloud(collocations = False, background_color = 'white').generate(text)
    plt.imshow(pil_img, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/new_plot.png')
    return render_template('index.html', name = 'new_plot', url ='/static/images/new_plot.png')

@app.route('/analyse')
def view_analyse():
    func('Fake',20)
    i = 0
    tweets = df['Tweet']
    for i in range(len(labels)):
        labels[i] += np.random.randint(0,6)
        i = i + 1 
    x_axis= ['Grievance', 'Incitement', 'Threats', 'Irony', 'Stereotypes', 'Inferiority']
    plt.bar(x_axis, labels,color=['cyan','red','purple','green', 'blue', 'black'])
    plt.savefig('./static/images/bar_plot.png')
    return render_template('index.html', name = 'new_graph', url = './static/images/bar_plot.png')

@app.route('/geoheatmap')
def get_geoheatmap():
    #take input as df['User_location']
    urls, names = geoheatmap.create_geoheatmap()
    return render_template('geoheatmap.html', url = urls, name = names)


@app.route("/query5")
def plot_category():
    data = pd.read_csv("./Emotion.csv",encoding='latin-1',header=None)
    data = data.sample(frac = 1)
    data=data[0:50]
    data['follower_count']=500089
    #ploting
    category = 0
    #request.form['category']
    
    get_negative_data=data.loc[data[0]==0]
    sorted_negative=get_negative_data.groupby([4]).size()
    sorted_negative=sorted_negative.sort_values(ascending=False)
    sorted_negative=sorted_negative[0:5]
    plt.bar(sorted_negative.index,sorted_negative,color='black')
    plt.savefig("./static/images/bar_plot_category_negative.png")
    get_positive_data=data.loc[data[0]==4]
    sorted_positive=get_positive_data.groupby([4]).size()

    sorted_positive=sorted_positive.sort_values(ascending=False)
    sorted_positive=sorted_positive[0:5]
    plt.bar(sorted_positive.index,sorted_positive,color='black')
    plt.savefig("./static/images/bar_plot_category_positive.png")

    sorted_followers_count_negative=get_negative_data.drop_duplicates(4)
    sorted_followers_count_negative=sorted_followers_count_negative.sort_values('follower_count',ascending=False)
    sorted_followers_count_negative=sorted_followers_count_negative[0:5]
    plt.bar(sorted_followers_count_negative[4],sorted_followers_count_negative['follower_count'],color='black')
    plt.savefig("./static/images/bar_plot_category_negative_followers.png")

    sorted_followers_count_positive=get_positive_data.drop_duplicates(4)
    sorted_followers_count_positive=sorted_followers_count_positive.sort_values('follower_count',ascending=False)
    sorted_followers_count_positive=sorted_followers_count_positive[0:5]
    plt.bar(sorted_followers_count_positive[4].index,sorted_followers_count_positive['follower_count'],color='black')
    plt.savefig("./static/images/bar_plot_category_positive_followers.png")

    a,b,c,d="/static/images/bar_plot_category_negative.png","/static/images/bar_plot_category_positive.png","/static/images/bar_plot_category_negative_followers.png","/static/images/bar_plot_category_positive_followers"


    return render_template('query10.html',name = 'new_plot', aa=a,bb=b,cc=c,dd=d)
# @app.route("/categorical")
# def view_second_page():
#     return render_template("index.html", title="Second page")

# @app.route('/live', methods=["GET"])
# def get_live():
#     return(render_template('live.html'))


# @app.route('/programme', methods=["GET"])
# def get_programme():
#     return(render_template('programme.html'))

# @app.route('/classement', methods=["GET"])
# def get_classement():
#     return(render_template('classement.html'))

# @app.route('/contact', methods=["GET"])
# def get_contact():
#     return(render_template('contact.html'))

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