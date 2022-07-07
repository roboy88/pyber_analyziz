#Add matplotlib inline magic command
%matplotlib inline

#import dependencies
import matplotlib.pyplot as plt
import pandas as pd
import os
#Files to load
city_data_to_load = os.path.join("C:/Users/raney/OneDrive/Desktop/Analysis_Projects/PyBer_Analysis/Resources/city_data.csv")
ride_data_to_load = os.path.join("C:/Users/raney/OneDrive/Desktop/Analysis_Projects/PyBer_Analysis/Resources/ride_data.csv")

city_data_df = pd.read_csv(city_data_to_load)
ride_data_df = pd.read_csv(ride_data_to_load)

city_data_df
city	driver_count	type
0	Richardfort	38	Urban
1	Williamsstad	59	Urban
2	Port Angela	67	Urban
3	Rodneyfort	34	Urban
4	West Robert	39	Urban
...	...	...	...
115	Bradshawfurt	7	Rural
116	New Ryantown	2	Rural
117	Randallchester	9	Rural
118	Jessicaport	1	Rural
119	South Saramouth	7	Rural
120 rows × 3 columns

ride_data_df.head(10)
city	date	fare	ride_id
0	Lake Jonathanshire	2019-01-14 10:14:22	13.83	5739410935873
1	South Michelleport	2019-03-04 18:24:09	30.24	2343912425577
2	Port Samanthamouth	2019-02-24 04:29:00	33.44	2005065760003
3	Rodneyfort	2019-02-10 23:22:03	23.44	5149245426178
4	South Jack	2019-03-06 04:28:35	34.58	3908451377344
5	South Latoya	2019-03-11 12:26:48	9.52	1994999424437
6	New Paulville	2019-02-27 11:17:56	43.25	793208410091
7	Simpsonburgh	2019-04-26 00:43:24	35.98	111953927754
8	South Karenland	2019-01-08 03:28:48	35.09	7995623208694
9	North Jasmine	2019-03-09 06:26:29	42.81	5327642267789
city_data_df.count()
city            120
driver_count    120
type            120
dtype: int64
city_data_df.isnull().sum()
city            0
driver_count    0
type            0
dtype: int64
city_data_df.dtypes
city            object
driver_count     int64
type            object
dtype: object
#Get the unique values of type of city
city_data_df["type"].unique()
array(['Urban', 'Suburban', 'Rural'], dtype=object)
# get the number of data points from each type of cities
city_data_df["type"].value_counts()
Urban       66
Suburban    36
Rural       18
Name: type, dtype: int64
#get the count from ride data
ride_data_df.count()
city       2375
date       2375
fare       2375
ride_id    2375
dtype: int64
ride_data_df.isnull().sum()
city       0
date       0
fare       0
ride_id    0
dtype: int64
ride_data_df.dtypes
city        object
date        object
fare       float64
ride_id      int64
dtype: object
pyber_data_df = pd.merge(ride_data_df,city_data_df,  on = ["city", "city"], how = "left")
pyber_data_df.head(10)
city	date	fare	ride_id	driver_count	type
0	Lake Jonathanshire	2019-01-14 10:14:22	13.83	5739410935873	5	Urban
1	South Michelleport	2019-03-04 18:24:09	30.24	2343912425577	72	Urban
2	Port Samanthamouth	2019-02-24 04:29:00	33.44	2005065760003	57	Urban
3	Rodneyfort	2019-02-10 23:22:03	23.44	5149245426178	34	Urban
4	South Jack	2019-03-06 04:28:35	34.58	3908451377344	46	Urban
5	South Latoya	2019-03-11 12:26:48	9.52	1994999424437	10	Urban
6	New Paulville	2019-02-27 11:17:56	43.25	793208410091	44	Urban
7	Simpsonburgh	2019-04-26 00:43:24	35.98	111953927754	21	Urban
8	South Karenland	2019-01-08 03:28:48	35.09	7995623208694	4	Urban
9	North Jasmine	2019-03-09 06:26:29	42.81	5327642267789	33	Urban
# get the urban cities
urban_cities_df = pyber_data_df[pyber_data_df["type"] == "Urban"]
urban_cities_df.head()
city	date	fare	ride_id	driver_count	type
0	Lake Jonathanshire	2019-01-14 10:14:22	13.83	5739410935873	5	Urban
1	South Michelleport	2019-03-04 18:24:09	30.24	2343912425577	72	Urban
2	Port Samanthamouth	2019-02-24 04:29:00	33.44	2005065760003	57	Urban
3	Rodneyfort	2019-02-10 23:22:03	23.44	5149245426178	34	Urban
4	South Jack	2019-03-06 04:28:35	34.58	3908451377344	46	Urban
# get the suburban cities
suburban_cities_df = pyber_data_df[pyber_data_df["type"] == "Suburban"]
suburban_cities_df.head()
city	date	fare	ride_id	driver_count	type
1625	Barronchester	2019-01-27 03:08:01	27.79	6653622887913	11	Suburban
1626	East Kentstad	2019-04-07 19:44:19	18.75	6575961095852	20	Suburban
1627	Lake Omar	2019-01-17 21:33:35	21.71	966911700371	22	Suburban
1628	Myersshire	2019-02-27 17:38:39	17.10	5706770909868	19	Suburban
1629	West Hannah	2019-04-19 01:06:59	37.78	2273047151891	12	Suburban
# get the rural cities
rural_cities_df = pyber_data_df[pyber_data_df["type"] == "Rural"]
rural_cities_df.head()
city	date	fare	ride_id	driver_count	type
2250	Randallchester	2019-04-13 11:13:31	43.22	1076079536213	9	Rural
2251	North Holly	2019-02-02 14:54:00	12.42	1985256326182	8	Rural
2252	Michaelberg	2019-03-27 18:27:34	54.85	4421836952718	6	Rural
2253	Lake Latoyabury	2019-02-23 21:12:24	47.90	3269652929887	2	Rural
2254	Lake Latoyabury	2019-05-06 08:57:56	51.80	4018025271936	2	Rural
#Get the number of rides in each urban cities
urban_ride_count_series = urban_cities_df.groupby(["city"]).count() ["ride_id"]
urban_ride_count_series.head()
city
Amandaburgh        18
Barajasview        22
Carriemouth        27
Christopherfurt    27
Deanville          19
Name: ride_id, dtype: int64
#Get the number of rides in each suburban cities
suburban_ride_count_series = suburban_cities_df.groupby(["city"]).count() ["ride_id"]
suburban_ride_count_series.head()
city
Barronchester    16
Bethanyland      18
Brandonfort      19
Colemanland      22
Davidfurt        17
Name: ride_id, dtype: int64
#Get the number of rides in each rural cities
rural_ride_count_series = rural_cities_df.groupby(["city"]).count() ["ride_id"]
rural_ride_count_series.head()
city
Bradshawfurt      10
Garzaport          3
Harringtonfort     6
Jessicaport        6
Lake Jamie         6
Name: ride_id, dtype: int64
#Get the average fare for each urban city type
urban_ride_average_series = urban_cities_df.groupby(["city"]).mean() ["fare"]
urban_ride_average_series.head()
city
Amandaburgh        24.641667
Barajasview        25.332273
Carriemouth        28.314444
Christopherfurt    24.501852
Deanville          25.842632
Name: fare, dtype: float64
#Get the average fare for each suburban city type
suburban_ride_average_series = suburban_cities_df.groupby(["city"]).mean() ["fare"]
suburban_ride_average_series.head()
city
Barronchester    36.422500
Bethanyland      32.956111
Brandonfort      35.437368
Colemanland      30.894545
Davidfurt        31.995882
Name: fare, dtype: float64
#Get the average fare for each rural city type
rural_ride_average_series = rural_cities_df.groupby(["city"]).mean() ["fare"]
rural_ride_average_series.head()
city
Bradshawfurt      40.064000
Garzaport         24.123333
Harringtonfort    33.470000
Jessicaport       36.013333
Lake Jamie        34.358333
Name: fare, dtype: float64
#Get the driver count for each urban city type. We use mean becaue this information is from City data and when we merge it cross joins with all cities
urban_driver_count_series = urban_cities_df.groupby(["city"]).mean() ["driver_count"]
urban_driver_count_series.head()
city
Amandaburgh        12.0
Barajasview        26.0
Carriemouth        52.0
Christopherfurt    41.0
Deanville          49.0
Name: driver_count, dtype: float64
#Get the driver count for each suburban city type
suburban_driver_count_series = suburban_cities_df.groupby(["city"]).mean() ["driver_count"]
suburban_driver_count_series.head()
city
Barronchester    11.0
Bethanyland      22.0
Brandonfort      10.0
Colemanland      23.0
Davidfurt        23.0
Name: driver_count, dtype: float64
rural_driver_count_series = rural_cities_df.groupby(["city"]).mean() ["driver_count"]
rural_driver_count_series.head()
city
Bradshawfurt      7.0
Garzaport         7.0
Harringtonfort    4.0
Jessicaport       1.0
Lake Jamie        4.0
Name: driver_count, dtype: float64
# Build the scatter plot of urban cities
plt.scatter(urban_ride_count_series, urban_ride_average_series)
<matplotlib.collections.PathCollection at 0x1f47dfc7700>

# Add the size of the markers as the number of driver count
plt.scatter(urban_ride_count_series, urban_ride_average_series, s= urban_driver_count_series)
<matplotlib.collections.PathCollection at 0x1f4000a6340>

#Urban Scatter plot
plt.scatter(urban_ride_count_series, 
            urban_ride_average_series, 
            s= urban_driver_count_series * 10, 
            color = "coral", 
            edgecolor = "black", 
            linewidth = 1, 
            alpha =0.8, 
            label = "Urban")
plt.title("PyBer Ride-Sharing Data (2019)")
plt.xlabel("Total number of Rides(Per City)")
plt.ylabel("Average Fare($)")
plt.grid()
plt.legend()
<matplotlib.legend.Legend at 0x1f4000f1f70>

#Suburban Scatter plot
plt.scatter(suburban_ride_count_series, 
            suburban_ride_average_series, 
            s= suburban_driver_count_series * 10, 
            color = "skyblue", 
            edgecolor = "black", 
            linewidth = 1, 
            alpha =0.8, 
            label = "Suburban")
plt.title("PyBer Ride-Sharing Data (2019)")
plt.xlabel("Total number of Rides(Per City)")
plt.ylabel("Average Fare($)")
plt.grid()
plt.legend()
<matplotlib.legend.Legend at 0x1f40116cb80>

#Rural Scatter plot
plt.scatter(rural_ride_count_series, 
            rural_ride_average_series, 
            s= rural_driver_count_series * 10, 
            color = "gold", 
            edgecolor = "black", 
            linewidth = 1, 
            alpha =0.8, 
            label = "Rural")
plt.title("PyBer Ride-Sharing Data (2019)")
plt.xlabel("Total number of Rides(Per City)")
plt.ylabel("Average Fare($)")
plt.grid()
plt.legend()
<matplotlib.legend.Legend at 0x1f4011e3e20>

# Scatter plot for all city types
plt.subplots(figsize=(10, 6))
plt.scatter(urban_ride_count_series, 
            urban_ride_average_series, 
            s= urban_driver_count_series * 10, 
            color = "coral", 
            edgecolor = "black", 
            linewidth = 1, 
            alpha =0.8, 
            label = "Urban")
plt.scatter(suburban_ride_count_series, 
            suburban_ride_average_series, 
            s= suburban_driver_count_series * 10, 
            color = "skyblue", 
            edgecolor = "black", 
            linewidth = 1, 
            alpha =0.8, 
            label = "Suburban")
plt.scatter(rural_ride_count_series, 
            rural_ride_average_series, 
            s= rural_driver_count_series * 10, 
            color = "gold", 
            edgecolor = "black", 
            linewidth = 1, 
            alpha =0.8, 
            label = "Rural")
plt.title("PyBer Ride-Sharing Data (2019)", fontsize = 20)
plt.xlabel("Total number of Rides(Per City)", fontsize = 12)
plt.ylabel("Average Fare($)", fontsize = 12)
plt.grid(True)
plt.legend()
plt.show()

# Scatter plot for all city types
plt.subplots(figsize=(10, 6))
plt.scatter(urban_ride_count_series, 
            urban_ride_average_series, 
            s= urban_driver_count_series * 10, 
            color = "coral", 
            edgecolor = "black", 
            linewidth = 1, 
            alpha =0.8, 
            label = "Urban")
plt.scatter(suburban_ride_count_series, 
            suburban_ride_average_series, 
            s= suburban_driver_count_series * 10, 
            color = "skyblue", 
            edgecolor = "black", 
            linewidth = 1, 
            alpha =0.8, 
            label = "Suburban")
plt.scatter(rural_ride_count_series, 
            rural_ride_average_series, 
            s= rural_driver_count_series * 10, 
            color = "gold", 
            edgecolor = "black", 
            linewidth = 1, 
            alpha =0.8, 
            label = "Rural")
plt.title("PyBer Ride-Sharing Data (2019)", fontsize = 20)
plt.xlabel("Total number of Rides(Per City)", fontsize = 12)
plt.ylabel("Average Fare($)", fontsize = 12)
plt.grid(True)
# Create a legend

lgnd  = plt.legend(fontsize = 12, mode = "Expanded",
                  scatterpoints = 1, loc = "best", title = "City types")
lgnd.legendHandles[0]._sizes = [75]
lgnd.legendHandles[1]._sizes = [75]
lgnd.legendHandles[2]._sizes = [75]

lgnd.get_title().set_fontsize(12)
# Incorporate a text label about circle size.
plt.text(42, 35, "Note: Circle size correlates with driver count per city.", fontsize="12")


# Save the figure.
plt.savefig("C:/Users/raney/OneDrive/Desktop/Analysis_Projects/PyBer_Analysis/analysis/Fig1.png")

plt.show()

# Get summary statistics.
urban_cities_df.describe()
fare	ride_id	driver_count
count	1625.000000	1.625000e+03	1625.000000
mean	24.525772	4.873485e+12	36.678154
std	11.738649	2.907440e+12	20.075545
min	4.050000	1.458810e+10	3.000000
25%	14.550000	2.400244e+12	22.000000
50%	24.640000	4.711188e+12	37.000000
75%	34.580000	7.451579e+12	52.000000
max	44.970000	9.991538e+12	73.000000
# Get summary statistics.
suburban_cities_df.describe()
fare	ride_id	driver_count
count	625.000000	6.250000e+02	625.000000
mean	30.970128	4.971015e+12	13.712000
std	10.677508	2.912410e+12	8.042372
min	12.050000	3.218337e+08	1.000000
25%	21.970000	2.364253e+12	5.000000
50%	30.750000	5.053221e+12	16.000000
75%	39.830000	7.551674e+12	21.000000
max	49.960000	9.917744e+12	25.000000
# Get summary statistics.
rural_cities_df.describe()
fare	ride_id	driver_count
count	125.000000	1.250000e+02	125.000000
mean	34.623440	4.647746e+12	4.296000
std	14.558046	2.887834e+12	2.691156
min	10.110000	2.684873e+10	1.000000
25%	19.900000	2.275364e+12	1.000000
50%	37.050000	4.023962e+12	4.000000
75%	47.070000	7.118047e+12	7.000000
max	58.550000	9.990581e+12	9.000000
# Get summary statistics.
urban_ride_count_series.describe()
count    66.000000
mean     24.621212
std       5.408726
min      12.000000
25%      21.000000
50%      24.000000
75%      28.000000
max      39.000000
Name: ride_id, dtype: float64
# Get summary statistics.
suburban_ride_count_series.describe()
count    36.000000
mean     17.361111
std       4.323707
min       9.000000
25%      14.000000
50%      17.000000
75%      19.250000
max      27.000000
Name: ride_id, dtype: float64
# Get summary statistics.
rural_ride_count_series.describe()
count    18.000000
mean      6.944444
std       2.508157
min       3.000000
25%       5.250000
50%       6.000000
75%       8.750000
max      12.000000
Name: ride_id, dtype: float64
# Calculate the mean of the ride count for each city type.
round(urban_ride_count_series.mean(),2), round(suburban_ride_count_series.mean(),2), round(rural_ride_count_series.mean(),2)
(24.62, 17.36, 6.94)
round(urban_ride_count_series.median(),2)
24.0
round(suburban_ride_count_series.median(),2)
17.0
round(rural_ride_count_series.median(),2)
6.0
round(urban_ride_count_series.mode(),2)
0    22
1    25
Name: ride_id, dtype: int64
round(suburban_ride_count_series.mode(),2)
0    17
Name: ride_id, dtype: int64
import numpy as np
import scipy.stats as sts
# Calculate the measures of central tendency for the ride count for the urban cities.
mean_urban_ride_count = np.mean(urban_ride_count_series)
print(f"The mean for the ride counts for urban trips is {mean_urban_ride_count:.2f}.")
The mean for the ride counts for urban trips is 24.62.
median_urban_ride_count = np.median(urban_ride_count_series)
print(f"The mean for the ride counts for urban trips is {median_urban_ride_count}.")
The mean for the ride counts for urban trips is 24.0.
mode_urban_ride_count = sts.mode(urban_ride_count_series)
print(f"The mean for the ride counts for urban trips is {mode_urban_ride_count}.")
The mean for the ride counts for urban trips is ModeResult(mode=array([22], dtype=int64), count=array([7])).
mean_suburban_ride_count = np.mean(suburban_ride_count_series)
print(f"The mean for the ride counts for urban trips is {mean_suburban_ride_count:.2f}.")
The mean for the ride counts for urban trips is 17.36.
median_suburban_ride_count = np.median(suburban_ride_count_series)
print(f"The mean for the ride counts for urban trips is {median_suburban_ride_count}.")
The mean for the ride counts for urban trips is 17.0.
mode_suburban_ride_count = sts.mode(suburban_ride_count_series)
print(f"The mean for the ride counts for urban trips is {mode_suburban_ride_count}.")
The mean for the ride counts for urban trips is ModeResult(mode=array([17], dtype=int64), count=array([7])).
mean_rural_ride_count = np.mean(rural_ride_count_series)
print(f"The mean for the ride counts for urban trips is {mean_rural_ride_count:.2f}.")
The mean for the ride counts for urban trips is 6.94.
median_rural_ride_count = np.median(rural_ride_count_series)
print(f"The mean for the ride counts for urban trips is {median_rural_ride_count}.")
The mean for the ride counts for urban trips is 6.0.
mode_rural_ride_count = sts.mode(rural_ride_count_series)
print(f"The mean for the ride counts for urban trips is {mode_rural_ride_count}.")
The mean for the ride counts for urban trips is ModeResult(mode=array([6], dtype=int64), count=array([5])).
# Get the fares for the urban cities.
urban_fares = urban_cities_df["fare"]
urban_fares.head()
0    13.83
1    30.24
2    33.44
3    23.44
4    34.58
Name: fare, dtype: float64
# Calculate the measures of central tendency for the average fare for the urban cities.
mean_urban_fares = np.mean(urban_fares)
print(f"The mean fare price for urban trips is ${mean_urban_fares:.2f}.")

median_urban_fares = np.median(urban_fares)
print(f"The median fare price for urban trips is ${median_urban_fares:.2f}.")

mode_urban_fares = sts.mode(urban_fares)
print(f"The mode fare price for urban trips is {mode_urban_fares}.")
The mean fare price for urban trips is $24.53.
The median fare price for urban trips is $24.64.
The mode fare price for urban trips is ModeResult(mode=array([22.86]), count=array([5])).
# Get the fares for the suburban cities.
suburban_fares = suburban_cities_df["fare"]
suburban_fares.head()
1625    27.79
1626    18.75
1627    21.71
1628    17.10
1629    37.78
Name: fare, dtype: float64
# Calculate the measures of central tendency for the average fare for the urban cities.
mean_suburban_fares = np.mean(suburban_fares)
print(f"The mean fare price for suburban trips is ${mean_suburban_fares:.2f}.")

median_suburban_fares = np.median(suburban_fares)
print(f"The median fare price for suburban trips is ${median_suburban_fares:.2f}.")

mode_suburban_fares = sts.mode(suburban_fares)
print(f"The mode fare price for suburban trips is {mode_suburban_fares}.")
The mean fare price for suburban trips is $30.97.
The median fare price for suburban trips is $30.75.
The mode fare price for suburban trips is ModeResult(mode=array([17.99]), count=array([3])).
# Get the fares for the suburban cities.
rural_fares = rural_cities_df["fare"]
rural_fares.head()
2250    43.22
2251    12.42
2252    54.85
2253    47.90
2254    51.80
Name: fare, dtype: float64
# Calculate the measures of central tendency for the average fare for the urban cities.
mean_rural_fares = np.mean(rural_fares)
print(f"The mean fare price for rural trips is ${mean_rural_fares:.2f}.")

median_rural_fares = np.median(rural_fares)
print(f"The median fare price for rural trips is ${median_rural_fares:.2f}.")

mode_rural_fares = sts.mode(rural_fares)
print(f"The mode fare price for rural trips is {mode_rural_fares}.")
The mean fare price for rural trips is $34.62.
The median fare price for rural trips is $37.05.
The mode fare price for rural trips is ModeResult(mode=array([37.05]), count=array([2])).
# Get the driver count data from the urban cities.
urban_drivers = urban_cities_df['driver_count']
urban_drivers.head()
0     5
1    72
2    57
3    34
4    46
Name: driver_count, dtype: int64
# Get the driver count data from the urban cities.
suburban_drivers = suburban_cities_df['driver_count']
suburban_drivers.head()
1625    11
1626    20
1627    22
1628    19
1629    12
Name: driver_count, dtype: int64
# Get the driver count data from the urban cities.
rural_drivers = rural_cities_df['driver_count']
rural_drivers.head()
2250    9
2251    8
2252    6
2253    2
2254    2
Name: driver_count, dtype: int64
# Calculate the measures of central tendency for the average fare for the urban cities.
mean_urban_drivers = np.mean(urban_drivers)
print(f"The mean number of drivers for urban is ${mean_urban_drivers:.0f}.")

median_urban_drivers = np.median(urban_drivers)
print(f"The median number of drivers for urban is ${median_urban_drivers:.0f}.")

mode_urban_drivers = sts.mode(urban_drivers)
print(f"The number of drivers for urban is  {mode_urban_drivers}.")
The mean number of drivers for urban is $37.
The median number of drivers for urban is $37.
The number of drivers for urban is  ModeResult(mode=array([39], dtype=int64), count=array([86])).
# Calculate the measures of central tendency for the average fare for the suburban cities.
mean_suburban_drivers = np.mean(suburban_drivers)
print(f"The mean number of drivers for suburban is ${mean_suburban_drivers:.0f}.")

median_suburban_drivers = np.median(suburban_drivers)
print(f"The median number of drivers for suburban is ${median_suburban_drivers:.0f}.")

mode_suburban_drivers = sts.mode(suburban_drivers)
print(f"The number of drivers for suburban is  {mode_suburban_drivers}.")
The mean number of drivers for suburban is $14.
The median number of drivers for suburban is $16.
The number of drivers for suburban is  ModeResult(mode=array([20], dtype=int64), count=array([79])).
# Calculate the measures of central tendency for the average fare for the rural cities.
mean_rural_drivers = np.mean(rural_drivers)
print(f"The mean number of drivers for rural is ${mean_rural_drivers:.0f}.")

median_rural_drivers = np.median(rural_drivers)
print(f"The median number of drivers for rural is ${median_rural_drivers:.0f}.")

mode_rural_drivers = sts.mode(rural_drivers)
print(f"The number of drivers for rural is  {mode_rural_drivers}.")
The mean number of drivers for rural is $4.
The median number of drivers for rural is $4.
The number of drivers for rural is  ModeResult(mode=array([1], dtype=int64), count=array([32])).
# Create a box-and-whisker plot for the urban cities ride count.
x_labels = ["Urban"]
fig, ax = plt.subplots()
ax.boxplot(urban_ride_count_series, labels=x_labels)
# Add the title, y-axis label and grid.
ax.set_title('Ride Count Data (2019)')
ax.set_ylabel('Number of Rides')
ax.set_yticks(np.arange(10, 41, step=2.0))
ax.grid()
plt.show()

# Add all ride count box-and-whisker plots to the same graph.
x_labels = ["Urban", "Suburban","Rural"]
ride_count_data = [urban_ride_count_series, suburban_ride_count_series, rural_ride_count_series]
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Ride Count Data (2019)',fontsize=20)
ax.set_ylabel('Number of Rides',fontsize=14)
ax.set_xlabel("City Types",fontsize=14)
ax.boxplot(ride_count_data, labels=x_labels)
ax.set_yticks(np.arange(0, 45, step=3.0))
ax.grid()
# Save the figure.
plt.savefig("analysis/Fig2.png")
plt.show()

# Get the city that matches 39 (the outliner)

urban_city_outlier  = urban_ride_count_series[urban_ride_count_series==39].index[0]
print(f"{urban_city_outlier } has the highest rider count.")
West Angela has the highest rider count.
# Create a box-and-whisker plot for the urban fare data.
x_labels = ["Urban"]
fig, ax = plt.subplots()
ax.boxplot(urban_fares, labels=x_labels)
# Add the title, y-axis label and grid.
ax.set_title("Ride Fare Data (2019)")
ax.set_ylabel("Fare($USD)")
ax.set_yticks(np.arange(0, 51, step=5.0))
ax.grid()
plt.show()
print("Summary Statistics")
urban_fares.describe()

Summary Statistics
count    1625.000000
mean       24.525772
std        11.738649
min         4.050000
25%        14.550000
50%        24.640000
75%        34.580000
max        44.970000
Name: fare, dtype: float64
# Add all ride count box-and-whisker plots to the same graph.
x_labels = ["Urban", "Suburban","Rural"]
ride_count_data = [urban_fares, suburban_fares, rural_fares]
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Ride Fare Data (2019)')
ax.set_ylabel('Number of Rides')
ax.set_ylabel("Fare($USD)")
ax.boxplot(ride_count_data, labels=x_labels)
ax.set_yticks(np.arange(0, 61, step=5.0))
ax.grid()
# Save the figure.
plt.savefig("analysis/Fig3.png")
plt.show()

# Create the box-and-whisker plot for the urban driver count data.
x_labels = ["Urban"]
fig, ax = plt.subplots()
ax.boxplot(urban_drivers,labels=x_labels)
# Add the title, y-axis label and grid.
ax.set_title('Driver Count Data (2019)')
ax.set_ylabel('Number of Drivers)')
ax.set_yticks(np.arange(0, 90, step=5.0))
ax.grid()
plt.show()
print("Summary Statistics")
urban_drivers.describe()

Summary Statistics
count    1625.000000
mean       36.678154
std        20.075545
min         3.000000
25%        22.000000
50%        37.000000
75%        52.000000
max        73.000000
Name: driver_count, dtype: float64
# Add all ride count box-and-whisker plots to the same graph.
x_labels = ["Urban", "Suburban","Rural"]
ride_count_data = [urban_drivers, suburban_drivers, rural_drivers]
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_title('Driver Count Data (2019)')
ax.set_ylabel('Number of Drivers)')
ax.set_ylabel("Fare($USD)")
ax.boxplot(ride_count_data, labels=x_labels)
ax.set_yticks(np.arange(0, 81, step=5.0))
ax.grid()
# Save the figure.
plt.savefig("analysis/Fig4.png")
plt.show()

# Get the sum of the fares for each city type.
sum_fares_by_type = pyber_data_df.groupby(["type"]).sum()["fare"]
sum_fares_by_type
type
Rural        4327.93
Suburban    19356.33
Urban       39854.38
Name: fare, dtype: float64
# Get the sum of all the fares.
total_fares = pyber_data_df["fare"].sum()
total_fares
63538.64
# Calculate the percentage of fare for each city type.
type_percents = sum_fares_by_type / total_fares * 100
type_percents
type
Rural        6.811493
Suburban    30.463872
Urban       62.724635
Name: fare, dtype: float64
# Calculate the percentage of fare for each city type.
type_percents = 100 * pyber_data_df.groupby(["type"]).sum()["fare"] / pyber_data_df["fare"].sum()
type_percents
type
Rural        6.811493
Suburban    30.463872
Urban       62.724635
Name: fare, dtype: float64
# Build the percentage of fares by city type pie chart.
plt.pie(type_percents, labels=["Rural", "Suburban", "Urban"])
plt.show()

# Build the percentage of fares by city type pie chart.
plt.pie(type_percents,
    labels=["Rural", "Suburban", "Urban"],
    colors=["gold", "lightskyblue", "lightcoral"],
    explode=[0, 0, 0.1],
    autopct='%1.1f%%',
    shadow=True, startangle=150)
plt.title("% of Total Fares by City Type")
# Show Figure
plt.show()

# Import mpl to change the plot configurations using rcParams.
import matplotlib as mpl
# Build Pie Chart
plt.subplots(figsize=(10, 6))
plt.pie(type_percents,
    labels=["Rural", "Suburban", "Urban"],
    colors=["gold", "lightskyblue", "lightcoral"],
    explode=[0, 0, 0.1],
    autopct='%1.1f%%',
    shadow=True, startangle=150)
plt.title("% of Total Fares by City Type")
# Change the default font size from 10 to 14.
mpl.rcParams['font.size'] = 14
# Save Figure
plt.savefig("analysis/Fig5.png")
# Show Figure
plt.show()

# Calculate the percentage of rides for each city type.
ride_percents = pyber_data_df.groupby(["type"]).count()["ride_id"] / pyber_data_df["ride_id"].count() * 100
ride_percents
type
Rural        5.263158
Suburban    26.315789
Urban       68.421053
Name: ride_id, dtype: float64
# Import mpl to change the plot configurations using rcParams.
import matplotlib as mpl
# Build Pie Chart
plt.subplots(figsize=(10, 6))
plt.pie(ride_percents,
    labels=["Rural", "Suburban", "Urban"],
    colors=["gold", "lightskyblue", "lightcoral"],
    explode=[0, 0, 0.1],
    autopct='%1.1f%%',
    shadow=True, startangle=150)
plt.title("% of Total Rides by City Type")
# Change the default font size from 10 to 14.
mpl.rcParams['font.size'] = 14
# Save Figure
plt.savefig("analysis/Fig6.png")
# Show Figure
plt.show()

# Calculate the percentage of rides for each city type.
dirver_percents = city_data_df.groupby(["type"]).sum()["driver_count"] / city_data_df["driver_count"].sum() * 100
dirver_percents
type
Rural        2.623613
Suburban    16.481668
Urban       80.894719
Name: driver_count, dtype: float64
# Import mpl to change the plot configurations using rcParams.
import matplotlib as mpl
# Build Pie Chart
plt.subplots(figsize=(10, 6))
plt.pie(dirver_percents,
    labels=["Rural", "Suburban", "Urban"],
    colors=["gold", "lightskyblue", "lightcoral"],
    explode=[0, 0, 0.1],
    autopct='%1.1f%%',
    shadow=True, startangle=150)
plt.title("% of Total Drivers by City Type")
# Change the default font size from 10 to 14.
mpl.rcParams['font.size'] = 14
# Save Figure
plt.savefig("analysis/Fig7.png")
# Show Figure
plt.show()

 