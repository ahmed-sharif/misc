

"""

total distance 
475.6
capacity    mpg     original_cost       station
11.9        27.4    14.98               6



102.0 99.9
    d = 102.0

    galon_spent = 102.0 / 27.4 = 3.722
    remaining = 11.9 - 3.722 = 8.178

    distane_to_next = 220.0 - 102.0 = 118

    driving_capability = 8.178 * 27.4 = 224.0772

    make_stop = NO

220.0 132.9
    d = 118
    galon_spent = 118 / 27.4 = 4.306
    remaining = 8.178 - 4.306 = 3.8720

    less or equal ..... make stop  = true
    ((11.9 - 3.8720) * 132.9 )/100 = 10.669 + 2 = 12.669
    remaining = 11.9

256.3 147.9

275.0 102.9

277.6 112.9

381.8 100.9
"""

stations = [
    (102.0, 99.9),
    (220.0, 132.9),
    (256.3, 147.9),
    (275.0, 102.9),
    (277.6, 112.9),
    (381.8, 100.9)
]

total_distance = 475.6
tank_capacity = 11.9
current_tank_capacity = tank_capacity
mpg =        27.4
original_cost=    14.98
total_stations=               6

so_far_travelled = 0

last_point = 0
money_total  = 0 
print "original", original_cost
for i, station in enumerate(stations):
    money_spent = 0
    dis , c = station

    d = dis - last_point
    galon_spent = d / mpg
    remaining = current_tank_capacity - galon_spent
    if i == len(stations) - 1:
        distane_to_next = total_distance - dis
    else:
        distane_to_next = stations[i + 1][0] - dis

    driving_capability = remaining * mpg
    current_tank_capacity = remaining
    if remaining > (tank_capacity / 2):
        if driving_capability < distane_to_next:

            # make stop
            current_tank_capacity = tank_capacity
            money_spent = ((tank_capacity - remaining) * c) / 100 + 2
            print "money spent",money_spent
        else:
            print "not stopping"
    else:
        # make stop
        current_tank_capacity = tank_capacity
        money_spent = ((tank_capacity - remaining) * c) / 100 + 2
        print "money spent",money_spent
    last_point = dis
    money_total += money_spent
print "money_total", money_total + original_cost