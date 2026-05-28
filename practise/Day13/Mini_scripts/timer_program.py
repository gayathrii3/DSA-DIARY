import time

time_input = int(input("Enter time in seconds : "))

for t in range(time_input, 0, -1):
    seconds = t % 60
    minutes = int(t / 60) % 60
    hours = int(t / 3600) % 24
    days = int(t / 3600)
    print(f"{days:02}:{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")