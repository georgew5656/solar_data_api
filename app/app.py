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
    datapoints = processed_data_table.find({'latitude' : latitude , 'longitude' : longitude,
                        'datetime': {'$gte' : time_start, '$lt' : time_end}})
    return json.dumps(datapoints)


if __name__ == '__main__':
    api.run()
