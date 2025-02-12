# DATE    Task2

import datetime

x = datetime.datetime.now()

yesterday = x - datetime.timedelta(days = 1)
tomorow = x + datetime.timedelta(days = 1)

print(x)
print(yesterday)
print(tomorow)