import json
import country_converter as coco
from datetime import datetime, timedelta
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import fiona
import json
import plotly
import plotly.express as px
import plotly.tools as tls


def create_geoheatmap():
	data = pd.read_csv('countries_of_the_world.csv')
	geo_df = map()
	geo_df = country_codes(geo_df)
	data = country_codes(data)
	df = pd.merge(left=geo_df, right=data, how='left', left_on='iso2_code', right_on='iso2_code')
	df.fillna(0, inplace=True)
	# data.rename(columns = {'Population':'hate', 'Area (sq. mi.)':'offensive', 'GDP ($ per capita)':'fake'}, inplace = True)
	df['hate'] = df['Population']
	df['offensive'] = df['Area (sq. mi.)']
	df['fake'] = df['GDP ($ per capita)']
	df['none'] = df['hate']
	df['not_fake'] = df['offensive']
	df['true'] = df['fake']
	df['satire'] = df['hate']
	df['misleading'] = df['offensive']
	df['false'] = df['fake']
	df['imposter'] = df['hate']
	df['manipulated'] = df['offensive']
	df['implicit'] = df['fake']
	df['explicit'] = df['hate']
	df['not_hate'] = df['offensive']
	df['incitement'] = df['fake']
	df['inferiority'] = df['hate']
	df['irony'] = df['offensive']
	df['stereotypical'] = df['fake']
	df['threatening'] = df['hate']
	df['white grievance'] = df['offensive']
	cols = ['hate', 'offensive', 'none', 'fake', 'not_fake', 'true', 'satire', 'misleading', 'false', 'imposter', 'manipulated', 'implicit', 'explicit', 'not_hate', 'incitement', 'inferiority', 'irony', 'stereotypical', 'threatening', 'white grievance']
	gjsons = create_maps(df, cols)
	urls = generate_urls(4)
	return gjsons, urls, cols

def create_maps(df, cols):
	ctr = 0
	gjsons = []
	for col in cols:
		ctr += 1
		# title = 'World Data: '+col
		# source = 'Source: https://www.kaggle.com/datasets/fernandol/countries-of-the-world'
		# vmin = df[col].min()
		# vmax = df[col].max()
		# cmap = 'viridis'
		# # Create figure and axes for Matplotlib
		# fig, ax = plt.subplots(1, figsize=(20, 8))
		# # Remove the axis
		# ax.axis('off')
		# df.plot(column=col, ax=ax, edgecolor='0.8', linewidth=1, cmap=cmap)
		# # Add a title
		# ax.set_title(title, fontdict={'fontsize': '25', 'fontweight': '3'})
		# # Create an annotation for the data source
		# ax.annotate(source, xy=(0.1, .08), xycoords='figure fraction', horizontalalignment='left', 
		#             verticalalignment='bottom', fontsize=10)
		# # Create colorbar as a legend
		# sm = plt.cm.ScalarMappable(norm=plt.Normalize(vmin=vmin, vmax=vmax), cmap=cmap)
		# # Empty array for the data range
		# sm._A = []
		# # Add the colorbar to the figure
		# cbaxes = fig.add_axes([0.15, 0.25, 0.01, 0.4])
		# cbar = fig.colorbar(sm, cax=cbaxes)

		# fig.savefig('./static/images/geoheatmap_plot_'+str(ctr)+'.png', dpi=300)

		plotly_fig = px.choropleth(df,
               geojson=df.geometry,
               locations=df.index,
               color=col,
               # hover_data=["Bergeron", "Coderre", "Joly"],
               projection="mercator"
        )
		plotly_fig.update_geos(fitbounds="locations", visible=False)
		graphJSON = json.dumps(plotly_fig, cls=plotly.utils.PlotlyJSONEncoder)
		gjsons.append(graphJSON)
	return gjsons


def specific_code(s):
	iso3_codes = s.to_list()
	iso2_codes_list = coco.convert(names=iso3_codes, to='ISO2', not_found='NULL')
	return pd.DataFrame(iso2_codes_list)

def country_codes(df):
	# Ensure that our data matches with the country codes. 
	if 'country' in df.columns:
		iso3_codes = df['country'].to_list()
	else:
		iso3_codes = df['Country'].to_list()
	# Convert to iso3_codes
	iso2_codes_list = coco.convert(names=iso3_codes, to='ISO2', not_found='NULL')
	# Add the list with iso2 codes to the dataframe
	df['iso2_code'] = iso2_codes_list
	# Drop countries without country code
	df = df.drop(df.loc[df['iso2_code'] == 'NULL'].index)
	return df

def map():
	# Setting the path to the shapefile
	SHAPEFILE = 'shapefiles/ne_10m_admin_0_countries.shp'
	# Read shapefile using Geopandas
	geo_df = gpd.read_file(SHAPEFILE)[['ADMIN', 'ADM0_A3', 'geometry']]
	# Rename columns
	geo_df.columns = ['country', 'country_code', 'geometry']
	# Drop row for 'Antarctica'
	geo_df = geo_df.drop(geo_df.loc[geo_df['country'] == 'Antarctica'].index)
	return geo_df

def generate_urls(n):
	urls = []
	for i in range(1, n+1, 1):
		urls.append('/static/images/geoheatmap_plot_'+str(i)+'.png')
	return urls