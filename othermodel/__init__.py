# datetime
from datetime import datetime,timedelta

dt = datetime(2015,10,1,12,20,22,22)
print(dt)
print(dt.timestamp())

t = 1443673222.000022
print(datetime.fromtimestamp(t))

strtime = datetime.strptime('2015-10-12','%Y-%m-%d')
print(strtime)
print(strtime.strftime('%a,%b %d %H:%M'))

now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now - timedelta(days=1,hours=2))


# 
