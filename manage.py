from db.models import SolarDataBiHourly, SolarDataDaily, SolarDataBiHourlyRaw, SolarDataDailyRaw
import pymodm
import sys
from flask_script import Manager
import os
from app.app import api
import json
import datetime

manager = Manager(api)


@manager.command
def load():
    if len(sys.argv < 2):
        print("Please enter a year of data to add to the database")
    pymodm.connect("mongodb://localhost:27017/solar_data")

    connection_path = "../solar_data/geojson_files/2012" #should take this as a argument
    filenames = os.listdir(connection_path)
    day_interval = 24 * 2
    for filename in filenames:
        with open (connection_path + '/' + filename) as f:
            data = json.load(f)
            location = filename.split(',')
            timeseries = data['Time_series']
            for i in range(len(timeseries['DateTime'])):
                day_date = timeseries['DateTime'].split(' ')
                if i % day_interval == 0:
                    raw_data_daily = SolarDataDailyRaw(timeseries['max_ramp_30_min'][int(i / day_interval)],
                                                       timeseries['max_ramp_60_min'][int(i / day_interval)],
                                                       timeseries['percentage_variability_per_day'][int(i / day_interval)])
                    data_daily = SolarDataDaily(datetime.date(2012, day_date[0], day_date[1]), location[0], location[1], raw_data_daily)
                    data_daily.save()
                raw_data_bihourly = SolarDataBiHourlyRaw(timeseries['GHI'][i],
                                                         timeseries['DNI'][i],
                                                         timeseries['generation'][i],
                                                         timeseries['Solar Zenith Angle'][i],
                                                         timeseries['DHI'][i],
                                                         timeseries['capacity_factor'][i],
                                                         timeseries['Temperature'][i],
                                                         timeseries['Wind Speed'][i])
                data_bihourly = SolarDataBiHourly(datetime.datetime(2012, day_date[0], day_date[1],
                                                                    int((i % day_interval)/2), i % 2 * 30),
                                                  location[0], location[1], raw_data_bihourly)
                data_bihourly.save()


if __name__ == '__main__':
    manager.run()