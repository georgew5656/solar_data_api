from flask import Flask, request
from datetime import datetime
from pymongo import MongoClient
import json


api = Flask(__name__)

client = MongoClient()
client.connect('localhost', 27017)

db = client.solar_data
raw_data_table = db.raw_data
processed_data_table = db.processed_data


@api.route('/raw', methods=['GET'])
def raw_data():
    latitude = request.args['latitude']
    longitude = request.args['longitude']
    time_start = datetime.fromtimestamp(request.args['start'])
    time_end = datetime.fromtimestamp(request.args['end'])
    datapoints = raw_data_table.find({'latitude' : latitude , 'longitude' : longitude,
                        'datetime': {'$gte' : time_start, '$lt' : time_end}})
    return json.dumps(datapoints)


@api.route('/processed', methods=['GET'])
def processed_data():
    latitude = request.args['latitude']
    longitude = request.args['longitude']
    time_start = datetime.fromtimestamp(request.args['start'])
    time_end = datetime.fromtimestamp(request.args['end'])
    datapoints = processed_data_table.find({'latitude': latitude, 'longitude' : longitude,
                        'datetime': {'$gte' : time_start, '$lt' : time_end}})
    return json.dumps(datapoints)



@api.route('/data_points', methods=['GET'])
def available_points():
    latitude_min = request.args['latitude_min']
    latitude_max = request.args['latitude_max']
    longitude_min = request.args['longitude_min']
    longitude_max = request.args['longitude_max']
    datapoints = raw_data_table.find({'latitude' : {'$gte': latitude_min, '$lt': latitude_max},
                                      'lontigude' : {'$gte': longitude_min, '$lt': longitude_max}})
    datapoints = list(map(lambda x : (x['latitude'], x['longitude']), datapoints))
    return json.dumps(datapoints)
