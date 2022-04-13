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
    return render_template('index.html',name = 'new_plot', url ='/static/images/new_plot.png')

@app.route("/categorical")
def view_second_page():
    return render_template("index.html", title="Second page")

@app.route('/geoheatmap', methods=['GET'])
def get_geoheatmap():
    return(render_template('geoheatmap.html'))

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