import json

infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

#json load function converts data into a format python can work with
#in this case creates giant dictionary
eq_data = json.load(infile)

#dump function takes json data and format into something more readable
#creates new file --> readable_eq_data.json
json.dump(eq_data,outfile, indent=4)


#to get just earthquake info, need key info of dicitonary
#value of features dictionary is a list, first earthquake has index 0
#get into eq_data (json readable file) to print out magnitude of first earthquake
#to get to first value of mag, use properties, then mag
#print(eq_data['features'][0]['properties']['mag'])


list_of_eqs = eq_data['features']
#features is key, and value of features is list of dictionaries --> so calling a list of earthquake dictionaries

mags, lons, lats = [], [], [] #three lists

#for loop to go through entire list of earthquakes
for eq in list_of_eqs:
    #eq is for each individual earthquake since each index of list is an earthquake
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])  #list slicing - print everything from first element to ninth element
print(lons[:10])
print(lats[:10])


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

#scatter geo allows us to plot scatterplots and plot on map
#latitiude and longitude creates layout and list of lat and long objects to plot on world map for you
#doing online means saving and seeing offline

data = [{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'marker':{#this is for the dots on map
        'size':[5*mag for mag in mags], #creates a list, going through mags list and for each item in mag list multiple by 5, result is another list that has all those values. Saving us for writing for loop
        'color': mags, #for each values in mag assigns a color
        'colorscale':'Viridis',
        'reversescale': True,
        'colorbar':{'title': 'Magnitude'}
    }
}]

my_layout = Layout(title='Global Earthquakes')

fig = {'data':data, 'layout':my_layout}  #outline function needs info of data and layout as function

offline.plot(fig, filename='global_earthquakes.html')








