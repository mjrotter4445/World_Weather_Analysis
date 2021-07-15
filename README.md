# World_Weather_Analysis
*An API World Weather Analysis*

## Project Overview 
### Purpose & Background

In this project I put together a beta version of an application for potential travel technology services that specializes in hotel and logging industry. The application collects and presents data for customers via the search page that can be filtered based on preferred travel criteria in order to find their ideal hotel anywhere in the world.
This project consists of three modules.
  -	Weather Database
  -	Vacation Search
  -	Vacation Itinerary
 
### Overview the methods and code
The data is gathered in two different CSV files (the city data and the ride data). We then utilize **Jupyter notebook** and **Pandas Library** to inspect data, and merge dataset.   
perform calculations and create new data series and data frames to work with.  We are also using Python’s plotting library **Matplotlib** to make the more effective charts. 

### Resources
- Data Sources :      CSV files here  
  - [PyBer_ride_data.csv](https://xx.csv)
  - [Vacation_Search.csv](https://github.com/mjrotter4445/World_Weather_Analysis/blob/main/Vacation_Search/WeatherPy_vacation.csv)
  - [ride_data.csv](https://xx.csv)

## Results 
The first exercise in this challenge was to create a DataFrame with our combined data.  The new Pyber Fare Summary looks like this: 

INSERT THE WEATHER DATABASE shots here  down below and rewrite this 
In this module I used NumPy random module to retrieve 2000 random coordinates (latitudes and longitudes) and CityPy module to define the closest city names based on these coordinates. Once city names were stored in a list, I used Open Weather APIs to request json weather data from a website. After cleaning the data, final results were transformed into Pandas data frame and stored in CSV file.

![xx](xx)
 
INSERT THE WEATHER DATABASE shots here  down below and rewrite this 
In this module I used input function to take and store potential customer preferred minimum and maximum temperatures. Based on this input I used Pandas loc method on Weather Database file to filter the data. Next, I used Google Maps APIs to retrieve hotel names. After cleaning the data, the data frame was exported to CSV file. With the Jupyter gmaps module I plotted map with pop-up message that includes hotel name, city, country and weather information.  The next exercise was to build a pivot table to display the comparitive results. From the pivot table we were able to  
prdouce and display more meaningful data.  This multi-line chart tells the story in detail and is pleasant to read. 
   
 ![Multiple Line Chart Tot Fares by City Type](https://xx.png)
 
 
INSERT THE VACATION ITINERARY  here and rewrite this stuff below  
In this module I selected 4 hotel destinations that potential customers might like to use for their trip planning. Based on selection I extracted coordinates with to_numpy() function and used Google Directions API to connect and mark those points via selected traveling mode
  ![Multiple Line Chart Tot Fares by City Type](https://xxy.png)
   ![Multiple Line Chart Tot Fares by City Type](https:/xx.png)
 
 
 
 
 
 just in case i need this  keep the format  
1. The total number of rides for each city type. 
   - Here we see that total ridership in Urban cities and higher that Suburban and most significantly higher than 
     Rural cities - by 13 times higher.  
2. The total number of drivers for each city type.
   - We also know that total drivers in Urban cities is much higher that in rural cities.The number of drivers
     in Urban type is almost 31 times higher than Rural.  
3. The sum of the fares for each city type.
   - The fares in Urban cities is much higher than Suburban and Rural. In some cases, 9 times higher.  
4. The average fare per ride for each city type.
   - The average fare per ride is lower in Urban cities. The most economical ride is costs an 
     average of $24.53 a ride
5. The average fare per driver for each city type.
   - Average fares are also lower in Urban cities than in Rural cities.  The average fare per driver 
     is most economical in the city at only $16.57 per driver
6. The total fares for each week by city type. The results below represent the 
   total Fares by City type and the Urban, Suburban, and Rural correlation between the average fares per week.    
   This data in the multi-line graph is from a period of time Jauary 2019 to May 2019.
