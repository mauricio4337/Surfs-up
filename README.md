# Surfs-up

* **Overview**
---
Use SQLAlchemy to connect to data stored in a SQLite file.  The file contains weather data for Honolulu.  The project is to help a Surf and Shaved Ice Shop determine if the shop can expect a significant drop in business during the off season due to weather concerns.  As part of the project, Flask was used to display weather data as API on a local host server.

* **Challenge**
---
The challenge required temperature data to be queried for the months of June and December.  Each data set was saved into a dataframe using Pandas and descriptive statistics were generated for each data set.  Analysis on the data is given below with recommendations for further analysis.

* **Analysis**
---
June Temperature Summary
![June Temp Stats](https://github.com/mauricio4337/Surfs-up/blob/master/June_Temps.png)


December Temperature Summary
![December Temp Stats](https://github.com/mauricio4337/Surfs-up/blob/master/December_Temps.png)

On first inspection of the data, the mean temperature and standard deviation are similar for both June and December (74.9, 71.0 respectively for average temperature and 3.25, 3.75 respectively for standard deviation).  However, the minimum temperature is 8 degrees lower for December than June.  This may not be a problem for the surf shop as it might reflect the overnight temperature drops significantly in the off season, but the daytime temperatures during business hours reflect suitable temperatures for steady business.  The first quartile for the temperatures shows only a four degree difference.
