import datetime
from datetime import timezone
import pytz

# d= datetime.date(2022 , 8 , 10)
# print(d)
# td = datetime.date.today()
# print(td.weekday())
# print(td.isoweekday())
# print(td.day)
# print(td.month)

# tdelta = datetime.timedelta(days=7)
# print(td+tdelta)
# bd = datetime.date(2022,8,10)
# till_bd = bd- td
# print(till_bd.total_seconds())

# t = datetime.time(12,9,50,12)
# print(t.hour)
# print(t.minute)

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# tdelta = datetime.timedelta(hours=7)
# print(dt_today+tdelta)

# dt = datetime.datetime(2022,7,27,12,30,45,tzinfo=timezone.utc)
# print(dt)

# dt_utcnow = datetime.datetime.now(tz=timezone.utc)
# print(dt_utcnow)

# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)

# for tz in pytz.all_timezones:
#     print(tz)

# dt_mtn = datetime.datetime.now() # naive
# mtn_tz = pytz.timezone('US/Mountain')
# dt_mtn = mtn_tz.localize(dt_mtn)

# print(dt_mtn)

dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))

print(dt_mtn.isoformat())

print(dt_mtn.strftime('%b'))

dt_str = 'July 26, 2022'

dt= datetime.datetime.strptime(dt_str, '%B %d, %Y')
