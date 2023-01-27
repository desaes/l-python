raw_time = 8594

minutes, seconds = divmod(raw_time, 60)
hours, minutes = divmod(minutes, 60)

print(f"{raw_time}s is {hours}h {minutes}m {seconds}s")
# 8594s is 2h 23m 14s