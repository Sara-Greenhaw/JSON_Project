#use fire files to compare files that have been burning in california 
#between Sep 1-13 and Sept 14-30
#file contains info about lat and lon and brightness of each fire
#make a map that shows the fires
#one file is from 9-1-20 to 9-13-20
#other file is 9-14-20-9-20-20
#only interested in fires that have brightness factor above 450

import json

infile = open('US_fires_9_1.json', 'r')
outfile = open('readable_US_fires_9_1.json', 'w')

#json load function converts data into a format python can work with
#in this case creates giant dictionary
fire_data = json.load(infile)

#dump function takes json data and format into something more readable

json.dump(fire_data,outfile, indent=4)

lons, lats, brights =  [], [], []

#go through entire list of fires!
#since out data is a list of dictionaries, and each dicitonary is a fire, can just use our file
for fire in fire_data:
    if int(fire['brightness']) > 450:
        lon = fire['longitude']
        lat = fire['latitude']
        bright = int(fire['brightness'])


        lons.append(lon)
        lats.append(lat)
        brights.append(bright)

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
#scatter geo allows us to plot scatterplots and plot on map
#latitiude and longitude creates layout and list of lat and long objects to plot on world map for you
#doing online means saving and seeing offline
data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker':{
        'size':[bright/20 for bright in brights], 
        'color': brights, #for each value in mag assigns a color
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar':{'title': 'Magnitude'}
    }
}]

my_layout = Layout(title='US Fires Above 450 Brightness 9/1/20 to 9/13/20')
fig = {'data':data, 'layout':my_layout}
offline.plot(fig, filename='fires_september.html')

