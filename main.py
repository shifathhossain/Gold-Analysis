import folium
from folium.plugins import MarkerCluster

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from data_cleaning import meteorites

# Create a base map centered at the equator with an initial zoom level of 2
m = folium.Map(location=[0, 0], zoom_start=2)

# Create a marker cluster to group close markers together for better visualization
marker_cluster = MarkerCluster().add_to(m)

# Loop through each row in the meteorites DataFrame and add a marker to the cluster
for index, row in meteorites.iterrows():
    # Extract the latitude and longitude from the row
    location = [row['reclat'], row['reclong']]
    
    # Create a popup message with meteorite details
    popup_message = (
        f"{row['name']} ({row['year']}), Mass: {row['mass (g)']}g, Class: {row['recclass']}"
    )
    
    # Create a marker with the location and popup message
    folium.Marker(
        location=location,
        popup=popup_message,
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(marker_cluster)

# Save the map to an HTML file
map_file_path = 'meteorite_landings_map.html'



# Bar chart for meteorite types
plt.figure(figsize=(12, 6))
sns.countplot(data=meteorites, x='recclass', order=meteorites['recclass'].value_counts().index)
plt.xticks(rotation=90)
plt.title('Distribution of Meteorite Types')
plt.xlabel('Meteorite Type')
plt.ylabel('Count')
plt.show()