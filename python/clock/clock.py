class Clock:
    def __init__(self, hour, minute):
        self.hours, self.minutes = divmod((hour*60 + minute)%(24*60), 60)

    @property
    def now(self):
        return f"{self.hours:02}:{self.minutes:02}"

    def __str__(self):
        return self.now

    def __eq__(self, other):
        return self.now == other

    def __add__(self, minutes):
        return Clock(self.hours, self.minutes + minutes)

    def __sub__(self, minutes):
        return Clock(self.hours, self.minutes - minutes)

