from flask_script import Manager
import os
from app.app import api
import json
from pymongo import MongoClient
from datetime import datetime

manager = Manager(api)
processed_data_fields = ['percentage_variability_per_day', 'max_ramp_30_min', 'max_ramp_60_min']
raw_data_fields = ['GHI', 'DNI', 'Temperature', 'Wind Speed', 'generation',
                   'Solar Zenith Angle', 'DHI', 'capacity_factor']

client = MongoClient()
client.connect('localhost', 27017)

@manager.command
def load(year):
    db = client.solar_data
    raw_data_collection = db.raw_data
    processed_data_collection = db.processed_data
    # should take this as a argument
    connection_path = "../solar_data/geojson_files/" + str(year)
    filenames = os.listdir(connection_path)
    for j, filename in enumerate(filenames):
        print(j)
        with open(connection_path + '/' + filename) as f:
            data = json.load(f)
            location = filename.split(',')
            timeseries = data['Time_series']
            raw_data_models = []
            processed_data_models = []
            for i in range(len(timeseries['DateTime'])):
                processed_data = {}
                raw_data = {}
                time_key = timeseries['DateTime'][i]
                spatial_data = {'datetime': datetime.strptime(time_key, "%B %d @ %H:%M").replace(year=int(year)),
                                'latitude': location[0], 'longitude': location[1]}
                for processed_data_name in processed_data_fields:
                    if time_key in timeseries[processed_data_name]:
                        processed_data[processed_data_name] = timeseries[processed_data_name][time_key]
                for raw_data_name in raw_data_fields:
                    if time_key in timeseries[raw_data_name]:
                        raw_data[raw_data_name] = timeseries[raw_data_name][time_key]
                raw_data_models.append(dict(raw_data, **spatial_data))
                processed_data_models.append(dict(processed_data, **spatial_data))
            raw_data_collection.insert(raw_data_models)
            processed_data_collection.insert(processed_data_models)


@manager.command
def runserver():
    api.run()

if __name__ == '__main__':
    manager.run()