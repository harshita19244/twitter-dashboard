from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from dominate.tags import img

app = Flask(__name__)
Bootstrap(app)

@app.route('/',methods = ['GET'])
def get_home():
    return(render_template('index.html'))

# @app.route('/visualize', methods=['GET'])
# def get_news():
#     return(render_template('news.html'))

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