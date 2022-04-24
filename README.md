# twitter-dashboard
### To run
1. Clone the repo and set up loacl flask environment in the directory you clone the repo
2. Cd to directory where the repo is
3. Run the following:
```
export FLASK_APP=main
export FLASK_ENV=development
python -m flask run

}
```

4. For windows based command line use set instead of export
  
  
#### For Geolocation heatmap
* Create a wheels/ folder
* Download whl files for Fiona and GDAL corresponding to your system from these links and add to the folder:
https://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona
https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal
* cd into the wheels/ folder
* pip install <wheel_file_name>


### For main2.py
* running this instead of main.py will create a database
* First pip install flask_sqlalchemy
* open a new terminal in the same folder and enter the following commands
* > python (this will open python)
* >>>from main import db
* >>>db.create_all()
* >>>exit()
* This will create twitter.db in the folder 
* now run the main.py and open the localhost:<port_num>/home
* open https://inloop.github.io/sqlite-viewer/ and upload twitter.db
* Here we can see the database getting updated with the real-time twitter data
