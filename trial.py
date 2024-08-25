from datetime import datetime
duration = (datetime.now().replace(microsecond=0)) - 2
duration = round((duration.total_seconds() / 60), 1)
print(duration)