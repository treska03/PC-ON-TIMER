import json


class TimeHandler:

    @staticmethod
    def unpack_seconds(seconds):
        seconds = int(seconds)
        hours = seconds // 3600
        seconds = seconds % 3600
        minutes = seconds // 60
        seconds = seconds % 60
        return hours, minutes, seconds

class DataReader:

    @staticmethod
    def get_data(file, *data):
        with open(file, "r") as config_file:
            loaded = json.load(config_file)
            for d in data:
                yield loaded[d]
