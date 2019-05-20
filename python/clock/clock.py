from datetime import datetime, timedelta

class Clock(object):
    def __init__(self, hour, minute):
        self.time = datetime(2019,1,1, (hour + minute//60)%24, minute%60)

    def __repr__(self):
        return self.time.strftime("%H:%M")

    def __eq__(self, other):
        return self.time == other.time

    def __add__(self, minutes):
        self.time += timedelta(minutes=minutes)
        return repr(self)

    def __sub__(self, minutes):
        self.time -= timedelta(minutes=minutes)
        return repr(self)
