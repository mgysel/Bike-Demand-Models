# COMP3901: Predicting Station-level Hourly Bike-Sharing Demand Using XGBoost and LSTM

This project applies XGBoost and Long Short-Term Memory (LSTM) to the problem of predicting station-level hourly bike-sharing demand. 

## Introduction

The world’s population is expected to increase by 2 billion people over the next 30 years.
This will mean a significant increase in motorized vehicle use, which will lead to more congestion, noise, pollution, and greenhouse gas emissions.
Bike-Sharing systems pose one possible solution to this problem by reducing motorized vehicle use. Bike-sharing systems are a shared transport service that allows for short-term bike rental at unattended urban locations. They can lead to numerous benefits including a reduction in congestion, noise, pollution, and greenhouse gas emissions and improved public health; however, we only see these benefits if the bike fleets are rebalanced well, as poor rebalancing often leads to increased traffic congestion due to the manual relocation of bikes. As a result, accurately predicting bike-demand is a significant component in actually seeing these benefits; moreover, that is the problem my research addresses.

## Data Sets

This study used two data sets: New York City Citi Bike bike-sharing demand data and National Oceanic and Atmospheric Administration (NOAA) meteorological data, from May 1st, 2019 to July 31st, 2019. 

The Citi Bike data set includes data on Citi Bike trips made throughout New York City, United States. More specifically, the Citi Bike data set includes station ID, station latitude and longitude, start time and date, stop time and date, start and end station names, station latitudes and longitudes, bike ID, user type, gender, and year of birth. The Citi Bike data set can be found <a href='https://www.citibikenyc.com/system-data' target='_blank'>here</a>. 

The NOAA meteorological data set includes meteorological data for a weather station located in Central Park in New York City, United States. More specifically, the NOAA data set includes daily minimum and maximum temperatures, precipitation, snowfall, snow depth, average wind speed, and the presence of specific weather types, such as fog, heavy fog, thunder, ice pellets, and numerous others. The NOAA data set can be found <a href='https://www.ncdc.noaa.gov/data-access' target='_blank'>here</a>. 

## Installation and Dependencies

Download the source code from the [master branch](https://github.com/mgysel/COMP3901---ML-Bike-Demand-Models).

Running the code requires Python 3.7.2 and JupyterLab 3.0.14. The following Python packages are also required: Pandas, Numpy, Matplotlib, Seaborn, Scipy, Sklearn, Tensorflow, and XGBoost. 

Next, navigate to the project folder from a terminal and run
```sh
$ jupyter notebook
```

This will automatically open the jupyter notebook!

## Notebooks

The following four notebooks were used:
* Data Cleaning: Clean the input data sets
* Data Analysis, Feature Engineering: Explore the cleaned data set and engineer features for the XGBoost and LSTM Models
* XGBoost: XGBoost model for predicting hourly station-level bike demand
* LSTM: LSTM model for predicting hourly station-level bike demand

## Conclusions


