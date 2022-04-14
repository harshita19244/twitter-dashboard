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
