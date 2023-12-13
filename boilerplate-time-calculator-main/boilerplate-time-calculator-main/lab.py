start = "11:59 PM"
duration = "24:05"
day = "Wednesday"

from time_calculator import time

# mytime = time(start=start, duration=duration)
# start = mytime.start_to_total_minutes()
# duration = mytime.duration_to_total_minutes()
# mytime.total_time()

pepe = time(start=start, duration=duration, day=day)
pepe.total_time()
print(pepe.day)