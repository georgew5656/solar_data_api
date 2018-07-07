from pymodm import MongoModel, fields

#Relic from using mymodm to access database, not currently used, will save just in case we would like to switch later


class SolarDataRaw(MongoModel):
    ghi = fields.FloatField(mongo_name="ghi")
    dni = fields.FloatField(mongo_name="dni")
    generation = fields.FloatField(mongo_name="generation")
    solar_angle = fields.FloatField(mongo_name="solar_angle")
    dhi = fields.FloatField(mongo_name="dhi")
    capacity_factor = fields.FloatField(mongo_name="capacity_factor")
    temperature = fields.FloatField(mongo_name="temperature")
    wind_speed = fields.FloatField(mongo_name="wind_speed")


class SpatialData(MongoModel):
    datetime = fields.DateTimeField(mongo_name='datetime')
    latitude = fields.FloatField(mongo_name='latitude')
    longitude = fields.FloatField(mongo_name='longitude')


class SolarDataProcessed(MongoModel):
    max_ramp_30 = fields.FloatField(mongo_name="max_ramp_30")
    max_ramp_60 = fields.FloatField(mongo_name="max_ramp_60")
    percent_variation = fields.FloatField(mongo_name="percent_variation")


class SolarData(MongoModel):
    raw_data = SolarDataRaw()
    processed_data = SolarDataProcessed()
    spatial_data = SpatialData()
