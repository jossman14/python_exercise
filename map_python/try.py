import folium
import pandas as pd

# peta dasar
map = folium.Map(location=[48.776798, -121.810997],
                 zoom_start=6, control_scale=True, tiles="Stamen Terrain")

# html type
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22+Mountain+%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

# ubah warna gunung


def ubah_warna(duwur):
    if duwur < 1000:
        return "green"
    elif 1000 < duwur < 2000:
        return "orange"
    else:
        return "red"


# import volcanoes data
data_vol = pd.read_csv("map_python/vol.txt")

vol = folium.FeatureGroup("peta saya")

for lt, ln, el, nm in zip(data_vol["LAT"], data_vol["LON"], data_vol["ELEV"], data_vol['NAME']):
    frame = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)
    vol.add_child(folium.CircleMarker([lt, ln], popup=folium.Popup(frame), tooltip=nm,
                                      fill_color=ubah_warna(el), color="grey", fill_opacity=0.7))

area = folium.FeatureGroup("area gan")
area.add_child(folium.GeoJson(
    data=open("map_python/world.json", "r", encoding="utf-8-sig").read(),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 1000000 else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red'}))

map.add_child(vol)
map.add_child(area)
map.add_child(folium.LayerControl())

map.save("peta.html")
