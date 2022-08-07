import json
import platform
from datetime import date, timedelta

try:
    import winsound
except ImportError:
    import os


class TimeHandler:

    @staticmethod
    def unpack_seconds(seconds):
        seconds = int(seconds)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        return hours, minutes, seconds
    
    @staticmethod
    def unpack_date(d):
        splitted = d.split("/")
        return int(splitted[2]), int(splitted[1]), int(splitted[0])
    
    @staticmethod
    def yield_dates_between(d1, d2):
        d1,d2 = date(*TimeHandler.unpack_date(d1)), date(*TimeHandler.unpack_date(d2))
        d1 = d1 + timedelta(1)
        for n in range(int((d2 - d1).days)+1):
            yield d1 + timedelta(n) 

class DataReader:

    @staticmethod
    def get_data(file, *data):
        with open(file, "r") as config_file:
            loaded = json.load(config_file)
            for d in data:
                yield loaded[d]

class PlaySound:

    @staticmethod
    def make_sound():
        system = platform.system()
        if system == "Windows":
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
        elif system == "Darwin" or system == "Linux":
            os.system(f'play -nq -t alsa synth 1 sine 440')
