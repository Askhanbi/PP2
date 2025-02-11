# DATE    Task3

import datetime

x = datetime.datetime.now()
y = int(x.strftime("%f"))

print(x - datetime.timedelta(microseconds = y))