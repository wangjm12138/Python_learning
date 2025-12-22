import time

print(time.time()) # timestamp
print(time.ctime()) # readability
print(time.localtime()) # local time


print(time.ctime(1699943418)) # given timestamp to return a readability object

print(time.gmtime()) # time tuple, zero zone

print(time.strftime('%Y-%m-%d %H:%M:%S'))

print(time.gmtime().tm_year)

import datetime

date  = datetime.datetime.now()
print(date.utcnow())
from datetime import date


date =  date(2025, 12, 31)
print(date)

print(date.timetuple())

print(date.strftime("%Y-%m-%d %H:%M:%S"))
print(date.weekday())


from datetime import time

t = time(10,58,39)
print(t)


from datetime import timedelta
td = timedelta(days=1, hours=1)
print(td)

f = datetime.datetime.now() + td
print(f)

ini_time_str = '2020/8/3 23:00:51'
end_time_str = '2020/9/3 23:00:51'


start = datetime.datetime.strptime(ini_time_str, '%Y/%m/%d %H:%M:%S')
end = datetime.datetime.strptime(end_time_str, '%Y/%m/%d %H:%M:%S')
tl = end - start
print(tl.days,tl.seconds,tl.microseconds)
