# Twitter-dashboard

### Abstract
Our project aims to develop an interactive tool that can perform fine-grained analysis and visualize diffusion patterns in real-time twitter data. So the aim is to classify data into fine-grained categories like authentic, fake,satire/parody, imposter, manipulated, hate speech, misleading content etc. The method opted to achieve the aim is by training our tool on state of the art models and further improving upon them using real-time Twitter data. We also aim to visualize content dispersion in real-time on social media using spatio-temporal heat maps and graphs as seen in Figure 8 and Figure 4. These factors, coupled together, will provide a comprehensive overview of information on social media and help us address how this information propagates and its extent of influencing opinions of online and offline social communities.

### Relevance
Social media content is immensely effective in altering politics and culture negatively. In the past, it has been observed to alter both online social network systems and offline communities and conversations. Automatic machine learning models often serve the purpose of detecting fake news and hate speech, but in order to combat the widespread dissemination of different kinds of fake information and hate speech, a more robust method is required. Moreover, looking into various tools that address the purpose, we observed that most tools classified social media information into broad categories of hate speech or fake news. A more fine-grained view into imposter, satire and manipulated content is not provided and very few tools address all these categories together. There is also a need for tools to visualize how this information propagates through social media, which may serve as a useful analytical tool to address the issue.


### Visualisations
Our interactive system is a website built using the Flask framework in Python. The frontend of the website uses HTML, CSS, and Javascript for a smooth user experience. Tweets are fetched in real-time using the Twitter API. Our models classify the tweets into the various categories. The data is then used to create the visualizations.
Bar Graph for category-wise tweets count: The bar graph shows the number of tweets under each category namely: Grievance, Incitement, Threats, Irony, Stereotypes and Inferiority, all of which identify as sub-categories of Hate Speech. Tweets are fetched in real-time using the Twitter API. The model takes the fetched tweet as an input and provides a simple classification prediction of the tweet. On the basis of the predictions made on the incoming tweets, the bar graph is updated dynamically as and when new tweets are fetched.

1. Category-wise Word Clouds: The category-wise word cloud represents the most occurring words in each of the identified categories. This visualization for the same was created using WordCloud, Stopwords, and ImageColorGenerator library functions.

2. Top users per category: This statistic essentially provides information about the most influential users in each category.  Hence, for each category and classification model, we plot a graph showing users that have tweeted the most in each category.


3. Category-wise Geolocation Heatmaps: The geolocation heatmap serves to visualize the countries having the most tweets in each category, on a world map. This visualization has been created using the Matplotlib and Geopandas library. A shapefile of the world provides the structure of the world map. Using realtime data of tweets, the location information corresponding to a tweet is fetched. This is further classified by the applied models to find a score corresponding to each country in the respective category. A heatmap is generated based on these scores which is visualised as a world map.

4. Dispersion network: The dispersion network serves to provide an insight into the way content is dispersed in our social media network. It helps us understand content dispersion patterns by providing a clear representation of connected users via their tweets and how this content propagates over a social network. The visualisation has been created using Javascript, which enables us to dynamically view the network as well as account for changes that occur within the network in real time. Corresponding to every tweet, we first fetch the associated users, shares and retweets associated with a particular tweet. These form connected components within the graph and help us visualize the network.

5. Real-time tweet classification: We additionally provide users with functionality to obtain the tone associated with their tweets in real-time. Users can therefore input their tweets in a query box and obtain predictions corresponding to different labels in real-time. This may provide users with additional insight as to how the tone of the tweet may be perceived. 



### How to Run
1. Clone the repo and set up loacl flask environment in the directory you clone the repo.
2. Cd to directory where the repo is.
3. Install all requirements using the following commannd:
```
pip install -r requirements.txt   #for Python 2
pip3 install -r requirements.txt  #for Python 3

```
5. Run the following:
```
export FLASK_APP=main
export FLASK_ENV=development
python -m flask run

```
4. For windows based command-line use set instead of export
  
  
#### Install Additional dependecies
* Create a wheels/ folder
* Download whl files for Fiona and GDAL corresponding to your system from these links and add to the folder:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona
https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal
* cd into the wheels/ folder
* pip install <wheel_file_name>

