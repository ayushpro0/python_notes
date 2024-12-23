file = open("10_sample.txt")

hour_count = {}

for line in file:
    if line.startswith('From'):
        words = line.split()
        time = words[5].split(":")[0]
        hour_count[time] = hour_count.get(time, 0) + 1

for hour in sorted(hour_count):
    print(hour, hour_count[hour])
