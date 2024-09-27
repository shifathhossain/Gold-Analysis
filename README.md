# Meteorite Landings Analysis 

This project aims to analyze global meteorite landings to uncover patterns in their distribution, composition, and temporal trends. Using NASA's Meteorite Landings dataset, we perform extensive data cleaning and visualization to gain insights into meteorite characteristics and their impact on Earth.

# Objectives
- Examine the temporal trends in the distribution of masses that have taken place over the years
- Visualize the individual variation in meteorite mass on a logarithmic scale to see potential outliers and patterns
- Compare the proportion of meteorites that were actively observed falling versus those which were found after the fact
  
# Dataset
Source: NASA's Meteorite Landings dataset

The dataset contains information about meteorite landings, including name, id, type, mass, fall date, latitude, longitude, and classification.

# Tools and Technologies
Programming Language: Python
Libraries:
Pandas - data manipulation
NumPy - numerical operations
Matplotlib and Seaborn - data visualization
Software: VS Code, Tableau


# Data Cleaning
- Handled missing values by forward filling
- Converted 'year' column to datetime format
- Ensured latitude and longitude columns were numeric
- Dropped rows with missing latitude or longitude values

# Visualizations
- Scatter Plot
- Bar Graph
- Pie Chart

You can explore the meteorite data in an interactive format via the following Tableau dashboard:
[View Meteorite Data Visualization on Tableau](https://public.tableau.com/views/MeteoriteDataVisualization/Sheet1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

