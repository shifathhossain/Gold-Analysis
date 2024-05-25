# Meteorite Landings Analysis 

This project aims to analyze global meteorite landings to uncover patterns in their distribution, composition, and temporal trends. Using NASA's Meteorite Landings dataset, we perform extensive data cleaning and visualization to gain insights into meteorite characteristics and their impact on Earth.

# Objectives
- Analyze the geographic distribution of meteorite landings
- Identify patterns and trends in meteorite composition
- Examine temporal trends in meteorite falls and possible correlations with other events.
  
# Dataset
Source: NASA's Meteorite Landings dataset

The dataset contains information about meteorite landings, including name, id, type, mass, fall date, latitude, longitude, and classification.

# Tools and Technologies
Programming Language: Python
Libraries:
Pandas - data manipulation
NumPy - numerical operations
Matplotlib and Seaborn - data visualization
Folium - geospatial visualization

# Data Cleaning
- Handled missing values by forward filling
- Converted 'year' column to datetime format
- Ensured latitude and longitude columns were numeric
- Dropped rows with missing latitude or longitude values


Descriptive Statistics: Summarized key metrics such as mass, geographic location, and classification of meteorites.

Geographic Distribution: Created an interactive map using Folium and MarkerCluster to display the geographic distribution of meteorite landings.

Temporal Trends: Visualized the number of meteorite landings over time using histograms and KDE plots.

Correlation Analysis: Explored correlations between different attributes such as mass, classification, and geographic location.

# Visualizations
Interactive Map: An interactive map showing meteorite landings with clustering for better visualization of dense areas

Histograms: Temporal analysis of meteorite landings over the years

Bar Charts: Distribution of meteorite types

Correlation Matrix: Heatmap showing correlations between numerical attributes
