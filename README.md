# solar_data_api

Companion API to Solar Data (https://github.com/jdlara-berkeley/solar_data)

Run scripts in solar_data to generate solar simulation data from NSRDB data,
and to generate processed data including variation and ramping.

Once data is in local directory, call manage.py script to load data into database (solar_data) and call manage.py script
again to run bare bones api.


API Information:

Raw Data:
Fields Returned- GHI, DNI, Temperature, Wind Speed, generation, Solar Zenith Angle, DHI, capacity_factor


Processed Data:
Fields Returned- percentage_variability_per_day, max_ramp_30_min, max_ramp_60_min


Datapoints:
Given min_latitude, max_latitude, min_longitude, max_longitude, return a list of the available data points inside the data box.


Call API with following Params:

latitude
longitude
start time, end time (python datetime timestamp string)
