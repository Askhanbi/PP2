# DATE    Task1

import datetime

x = datetime.datetime.now()

FiveDayBefore = x - datetime.timedelta(days=5)

print(FiveDayBefore)