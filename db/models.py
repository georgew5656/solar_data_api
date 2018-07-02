from pymodm import MongoModel, fields


class SolarDataBiHourlyRaw(MongoModel):
    ghi = fields.FloatField()
    dni = fields.FloatField()
    generation = fields.FloatField()
    solar_angle = fields.FloatField()
    dhi = fields.FloatField()
    capacity_factor = fields.FloatField()
    temperature = fields.FloatField()
    wind_speed = fields.FloatField



class SolarDataBiHourly(MongoModel):
    datetime = fields.DateTimeField(primary_key=True)
    latitude = fields.FloatField(primary_key=True)
    longitude = fields.FloatField(primary_key=True)
    raw_data = SolarDataBiHourlyRaw()


class SolarDataDailyRaw(MongoModel):
    max_ramp_30 = fields.FloatField()
    max_ramp_60 = fields.FloatField()
    percent_variation = fields.FloatField()


class SolarDataDaily(MongoModel):
    datetime = fields.DateTimeField(primary_key=True)
    latitude = fields.FloatField(primary_key=True)
    longitude = fields.FloatField(primary_key=True)
    raw_data = SolarDataDailyRaw()
