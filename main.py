import logging
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
import subprocess
from models.hsol import caller as cl1
from models.fakeddit_2 import caller as cl2
from models.fakeddit_6 import caller as cl3
matplotlib.use('Agg')

import geoheatmap
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
            # df.loc[i,"Coordinates"] = tweet.coordinates
            # df.loc[i,"Places"] = tweet.place
            #df.to_csv("TweetDataset.csv",index=False)
            #df.to_excel('{}.xlsx'.format("TweetDataset"),index=False)   ## Save as Excel
            i = i+1
            if i > Count:
                break
            else:
                pass
    # print(df["User_location"]
    df.to_csv("TweetDataset.csv",index=False)
    
@app.route('/home',methods = ['GET'])
def get_home():
    return render_template('primary.html')
    
@app.route('/wordcloud')
def view_wordcloud():
    func('Hate',20)
    pred = cl1(df)
    # 1 - OFFENSIVE
    # 0 - HATE
    # 2 - NEITHER
    #text = df['Tweet'][0]
    hate_tweets = pred.loc[pred['Category'] == 0]
    offensive_tweets = pred.loc[pred['Category'] == 1]
    none_tweets = pred.loc[pred['Category'] == 2]
    #print(hate_tweets)
    pil_img = WordCloud(collocations = False, background_color = 'white').generate(' '.join(hate_tweets['Tweet']))
    pil_img2 = WordCloud(collocations = False, background_color = 'white').generate(' '.join(offensive_tweets['Tweet']))
    pil_img3 = WordCloud(collocations = False, background_color = 'white').generate(' '.join(none_tweets['Tweet']))
    plt.imshow(pil_img, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wordcloud_plot1.png')
    plt.imshow(pil_img2, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wordcloud_plot2.png')
    plt.imshow(pil_img3, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/wordcloud_plot3.png')
    names = []
    names.append(pil_img);names.append(pil_img2);names.append(pil_img3)
    urls = []
    urls.append('./static/images/wordcloud_plot1.png');urls.append('./static/images/wordcloud_plot2.png');urls.append('./static/images/wordcloud_plot3.png')
    return render_template('index.html', name = names, url =urls)

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


@app.route('/geoheatmap')
def view_geoheatmap():
    func('Fake',500)
    graphJSON, urls, names = geoheatmap.create_geoheatmap()
    return render_template('geoheatmap.html', url = urls, name = names, graphJSON=graphJSON)

@app.route("/query5")
def plot_users():

    func('Fake',10000)
    data = cl3(df)
    count=[0,0,0,0,0,0]
    for i in range(len(count)):
        count[i]=len(data.loc[data['Category']==i])


    #data2=cl3(df)
    for i in count:
        app.logger.info("count")
        app.logger.info(i)
    #app.logger.info(data2.loc[0])
    

    get_0_data=data.loc[data['Category']==0]
    sorted_0=get_0_data.groupby("User").size()
    sorted_0=sorted_0.sort_values(ascending=False)
    sorted_0=sorted_0[0:5]
    fig = px.bar(x=sorted_0.index, y=sorted_0)
    fig.update_coloraxes(showscale=False)
    #fig.update_layout(x='UserName',y='#Likes')
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
    app.logger.info("count_likes 0")
    app.logger.info(len(sorted_likes_count_0))
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
    sorted_likes_count_1=sorted_likes_count_1[0:5]
    app.logger.info("count likes 1")
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
    app.logger.info("count_likes 2")
    app.logger.info(len(sorted_likes_count_2))
    sorted_likes_count_2=sorted_likes_count_2[0:5]
    fig = px.bar(x=sorted_likes_count_2["User"], y=sorted_likes_count_2["Likes"])
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# Likes")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_likes_2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    sorted_likes_count_3=get_3_data.drop_duplicates("User")
    sorted_likes_count_3=sorted_likes_count_3.sort_values("Likes",ascending=False)
    app.logger.info("count_likes 3")
    app.logger.info(len(sorted_likes_count_3))
    sorted_likes_count_3=sorted_likes_count_3[0:5]
    fig = px.bar(x=sorted_likes_count_3["User"], y=sorted_likes_count_3["Likes"])
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# Likes")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_likes_3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    sorted_likes_count_4=get_4_data.drop_duplicates("User")
    sorted_likes_count_4=sorted_likes_count_4.sort_values("Likes",ascending=False)
    app.logger.info("count_likes 4")
    app.logger.info(len(sorted_likes_count_4))
    sorted_likes_count_4=sorted_likes_count_4[0:5]
    fig = px.bar(x=sorted_likes_count_4["User"], y=sorted_likes_count_4["Likes"])
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# Likes")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_likes_4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    sorted_likes_count_5=get_5_data.drop_duplicates("User")
    sorted_likes_count_5=sorted_likes_count_5.sort_values("Likes",ascending=False)
    app.logger.info("count_likes 5")
    app.logger.info(len(sorted_likes_count_5))
    sorted_likes_count_5=sorted_likes_count_5[0:5]
    fig = px.bar(x=sorted_likes_count_5["User"], y=sorted_likes_count_5["Likes"])
    app.logger.info('after plotting fig')
    fig.update_coloraxes(showscale=False)
    fig.update_layout(xaxis_title="Users",yaxis_title="# Likes")
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis={'showticklabels': False})
    graphJSON_likes_5 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    

    return render_template('query10.html', graphJSON0=graphJSON0, graphJSON1=graphJSON0, graphJSON2=graphJSON2, graphJSON3=graphJSON3, graphJSON4=graphJSON4,graphJSON5=graphJSON5,graphJSON_likes_0=graphJSON_likes_0,graphJSON_likes_1=graphJSON_likes_0,graphJSON_likes_2=graphJSON_likes_2,graphJSON_likes_3=graphJSON_likes_3,graphJSON_likes_4=graphJSON_likes_4,graphJSON_likes_5=graphJSON_likes_5)


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
