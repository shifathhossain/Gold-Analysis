import folium
from folium.plugins import MarkerCluster

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from data_cleaning import meteorites

m = folium.Map(location=[0, 0], zoom_start=2)

marker_cluster = MarkerCluster().add_to(m)

for index, row in meteorites.iterrows():
    location = [row['reclat'], row['reclong']]

    popup_message = (
        f"{row['name']} ({row['year']}), Mass: {row['mass (g)']}g, Class: {row['recclass']}"
    )
    
    folium.Marker(
        location=location,
        popup=popup_message,
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(marker_cluster)

map_file_path = 'meteorite_landings_map.html'

plt.figure(figsize=(12, 6))
sns.countplot(data=meteorites, x='recclass', order=meteorites['recclass'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Distribution of Meteorite Types')
plt.xlabel('Meteorite Type')
plt.ylabel('Count')
plt.show()