import folium
map = folium.Map(location=[45.372,-121.697],zoom_start=12,tiles='Stamen Terrain')

folium.Marker([45.3288,-121.6625], popup='Mt. Hood Meadows').add_to(map)

folium.Marker([45.3311,-121.7311], popup='Timber Lake').add_to(map)

# map.simple_marker(location=[45.3288,-121.6625],popup='Mt. Hood Meadows', marker_color='red') no object to map found
# map.simple_marker(location=[45.3311,-121.7311],popup='Timber Lake', marker_color='green')
map.save('test2.html')
