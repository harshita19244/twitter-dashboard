# Twitter-dashboard

### Description
Social media content is immensely effective in altering politics and culture negatively. In the past, it has been observed to alter both online social network systems and offline communities and conversations. Automatic machine learning models often serve the purpose of detecting fake news and hate speech, but in order to combat the widespread dissemination of different kinds of fake information and hate speech, a more robust method is required. Moreover, looking into various tools that address the purpose, we observed that most tools classified social media information into broad categories of hate speech or fake news. A more fine-grained view into imposter, satire and manipulated content is not provided and very few tools address all these categories together. There is also a need for tools to visualize how this information propagates through social media, which may serve as a useful analytical tool to address the issue.

### How to Run
1. Clone the repo and set up loacl flask environment in the directory you clone the repo.
2. Cd to directory where the repo is.
3. Run the following:
```
export FLASK_APP=main
export FLASK_ENV=development
python -m flask run

```
4. For windows based command line use set instead of export
  
  
#### Install Additional dependecies
* Create a wheels/ folder
* Download whl files for Fiona and GDAL corresponding to your system from these links and add to the folder:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona
https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal
* cd into the wheels/ folder
* pip install <wheel_file_name>

