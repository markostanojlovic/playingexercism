from datetime import datetime, timedelta, date

class MeetupDayException(Exception):
    pass

DAY_OF_WEEK = { 'Monday' : 1, 'Tuesday' : 2, 'Wednesday' : 3, 'Thursday' : 4, 'Friday' : 5, 'Saturday' : 6, 'Sunday' : 7 }
WHICH = { '1st' : 0, '2nd' : 1, '3rd' : 2, '4th' : 3, '5th': 4, 'last' : -1 }

def meetup_day(year, month, day_of_the_week, which):
    mapping = { 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[] }
    d = datetime(year, month, 1)
    if month == 12 :
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year
    while d < datetime(next_year, next_month, 1):
        mapping[d.isoweekday()].append(d.day)
        d += timedelta(days=1)
    days = mapping[DAY_OF_WEEK[day_of_the_week]]
    if which == 'teenth':
        day = [ i for i in range(13,20) if i in days][0]
    else:
        try:
            day = days[WHICH[which]]
        except:
            raise MeetupDayException("Out of range")
    return date(year, month, day)
