import folium
import pandas


df = pandas.read_csv("Volcanoes-USA.txt")
df['NAME'] = df['NAME'].str.replace("'", "&#39;")
latmean = df['LAT'].mean()
lonmean = df['LON'].mean()
map = folium.Map(location=[0,0],zoom_start=3,tiles='Mapbox bright')

def color(elev):
    mini =int(min(df['ELEV']))
    step =int((max(df['ELEV'])-min(df['ELEV']))/4)
    if elev in range(mini,mini+step):
        col = 'green'
    elif elev in range (mini+step,mini+step*2):
        col = 'blue'
    elif elev in range(mini+step*2,mini+step*3):
        col = 'orange'
    else:
        col = 'red'
    return col

fg=folium.FeatureGroup(name="Volcano Locations")
for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    fg.add_child(folium.Marker(location=[lat,lon],popup=name, icon = folium.Icon(color = color(elev), icon = 'cloud',icon_color='green')))
map.add_child(folium.GeoJson(data=open('World_Population.json','r',encoding = 'utf-8-sig').read(),name ='World population',
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000<x['properties']['POP2005']<20000000 else 'red'}))
map.add_child(fg)
map.add_child(folium.LayerControl())

# Use above or below command to add marker
    #folium.Marker([lat,lon], popup=name,icon = folium.Icon(color = color(elev), icon = 'cloud')).add_to(map)
# https://stackoverflow.com/questions/46269861/html-page-is-blank-after-using-folium-to-create-map  Read the article
# folium.Marker([45.3311,-121.7311], popup='Timber Lake').add_to(map
# map.simple_marker(location=[45.3288,-121.6625],popup='Mt. Hood Meadows', marker_color='red') no object to map found
# map.simple_marker(location=[45.3311,-121.7311],popup='Timber Lake', marker_color='green')
map.save(outfile='test3.html')
