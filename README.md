# World_Weather_Analysis
*An API World Weather Analysis*

## Project Overview 
### Purpose & Background

In this project I put together a beta version of an application for potential travel technology services that specializes in hotel and 
logging industry.  The application collects and presents data for customers via the search page that can be filtered based on preferred 
travel criteria in order to find their ideal hotel anywhere in the world.

This project consists of three modules.

  -	Weather Database 
  -	Vacation Search  
  -	Vacation Itinerary
 
### Overview the methods and code
The data used to accomplish the activity are primarily 2 different CSV files (the weather data and the cleaned preferred hotel data). 
We then utilize **Jupyter notebook** and **Pandas Library** to inspect data, and merge datasets, perform calculations and create 
new data series and charts and maps.  We are also using **Matplotlib** to and data frames to work with Python’s plotting 
library make the more effective charts.

### Resources
- Data Sources :    
  - [WeatherPy_Database.csv](https://github.com/mjrotter4445/World_Weather_Analysis/blob/main/Weather_Database/WeatherPy_Database.csv)
  - [Vacation_Search.csv](https://github.com/mjrotter4445/World_Weather_Analysis/blob/main/Vacation_Search/WeatherPy_vacation.csv)


- Environment:  PythonData
- Dependencies: 
  -   Pandas Library
  -   Citipy Module
  -   Numpy Library
  -   Python Requests 
 - APIs: 
  -   Open Weather Maps API to retreive weather data.
  -   Google Maps API to create heat maps and retrieve information about hotels around the world.
  -   Google Directions APIto map the course between 4 points 
 
## Results 
 **1.   Weather Database**
The first exercise in this challenge was to create a DataFrame with our weather data that looks like this: 
In this activity we used **NumPy** to retrieve a random set of 2000 random coordinates (latitudes and longitudes)
and **Citipy** module to define the closest city names based on these coordinates.  Once the city names were stored 
in a list, we used **Open Weather APIs** to request **json** format weather data from the website.  After cleaning the data, 
final formats were developed into **Pandas** data frame and stored in CSV file.

<p align="center">
<img src="https://github.com/mjrotter4445/World_Weather_Analysis/blob/main/Weather_Database/WeatherPy_Dataframe_screenshot.png">
</p>

<p align="center">
Map by Google Maps APIs
</p>

**2.  Vacation Search** 
In this activity we used the input function to collect and store possible preferred minimum and maximum temperatures
desired for their vacation.   Based on this input, we used Pandas loc method on the Weather Database file to filter 
data.  Next, we applied Google Maps APIs to retrieve hotel names, clean the dta and export the file to a csv format.
With **Jupyter gmaps module** we can plot a map with markers at desired locations.      
         
![WeatherPy_travel_map_markers png](https://github.com/mjrotter4445/World_Weather_Analysis/blob/main/Vacation_Search/WeatherPy_vacation_map.png)
 
<p align="center">
Map by Google Maps APIs
</p>


**3.  Vacation Itinerary** 
In this activity we narrow the search.  We selected 4 hotel destinations that potential customers might like to use for their trip planning. 
Once the traveller selects the temperature range they prefer, we extracted coordinates **with to_numpy() function**
and used **Google Directions API** to connect and mark those points via selected traveling mode. 
  
 
  ![WeatherPy_travel_map png](https://github.com/mjrotter4445/World_Weather_Analysis/blob/main/Vacation_Itinerary/WeatherPy_travel_map_markers.png)
  
<p align="center">
Map of 4 hotels in Brazil we could travel to by Google Maps APIs
</p>

  
  ![WeatherPy_travel_map_markers png](https://github.com/mjrotter4445/World_Weather_Analysis/blob/main/Vacation_Itinerary/WeatherPy_travel_map.png)

<p align="center">
Map of the Driving Route we could take by Google Maps APIs
</p>

 

  
