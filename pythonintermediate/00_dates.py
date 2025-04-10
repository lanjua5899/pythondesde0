### Dates ###

# Date Time

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

now = datetime.now()


def print(now.day)


print(now.hour)
print(now.minute)
print(now.second)
print(now.year)
print(now.month)
print(now.timestamp())


print_date(now)

year_2025 = date(2025, 1, 1)

print_date(year_2025)

# Time

current_time = time(23, 59, 59)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# Date

current_date = date.today()

print(current_date.year)
print(current.date.month)
print(current.date.day)

current_date = date(2024, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)

print(current_date.month)

# Operaciones con fechas

diff = year_2025 - now
print(diff)

diff = year_2025.date() - current_date
print(diff)

# Timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
