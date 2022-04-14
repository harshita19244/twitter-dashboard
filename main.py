from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from dominate.tags import img
import numpy as np
import pandas as pd
from os import path
from PIL import Image

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')

import geoheatmap

app = Flask(__name__)


@app.route('/',methods = ['GET'])
def get_home():
    return render_template('primary.html')
    
@app.route('/visualize')
def view_visualise():
    df = pd.read_csv("./hatespeech.csv")
    text = df.tweet[0]
    pil_img = WordCloud(collocations = False, background_color = 'white').generate(text)
    plt.imshow(pil_img, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('./static/images/new_plot.png')
    return render_template('index.html', name = 'new_plot', url ='/static/images/new_plot.png')

@app.route('/geoheatmap')
def get_geoheatmap():
    urls, names = geoheatmap.create_geoheatmap()
    return render_template('geoheatmap.html', url = urls, name = names)
    # return
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