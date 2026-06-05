#program to take the lap times from n racers nd displaying fastest,slowest racer postion and finding its difference
racers=int(input("Enter the number of racers: "))
lap_time=float(input("Enter lap time of racer 1: "))
fastest_time = lap_time
slowest_time = lap_time
fastest_pos = 1
slowest_pos = 1
# Input remaining racers
for i in range(2, racers + 1):
    lap_time = float(input(f"Enter lap time of Racer {i}: "))
    if lap_time < fastest_time:
        fastest_time = lap_time
        fastest_pos = i
    if lap_time > slowest_time:
        slowest_time = lap_time
        slowest_pos = i
difference = slowest_time - fastest_time
print("Fastest Racer Position:", fastest_pos)
print("Slowest Racer Position:", slowest_pos)
print("Difference Between Fastest and Slowest Lap Time:", difference)

    