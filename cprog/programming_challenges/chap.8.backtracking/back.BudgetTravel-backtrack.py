
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
    money_to_fill = galon_spent * 99.9 + 200
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
all_costs = []
a = [0, 0, 0, 0, 0, 0]

def is_a_solution(a, k, n):
    return k == n

def process_solution(a, k, n):
    
    total = 0
    for x in a:
        total += x[1]
    # print total/100 + original_cost, a
    # print a, total/100 + original_cost
    all_costs.append(total/100 + original_cost)

def construct_candidates(a, k, n, last_point):
    #print a, k, n, last_point
    candidates = []
    st = stations[k - 1]
    dis , cost = st

    if k == 1:
        current_tank_capacity = tank_capacity
    else:
        current_tank_capacity = a[k - 1 -1][0]

    travelled_dis = dis - last_point
    # print "travelled",travelled_dis
    galon_spent = travelled_dis / mpg
    remaining_galon = current_tank_capacity - galon_spent

    if k == n:
        distane_to_next = total_distance - dis
    else:
        distane_to_next = stations[k][0] - dis

    how_many_more_miles_cango =  remaining_galon * mpg   
    fuelling_cost = (galon_spent + tank_capacity - current_tank_capacity) * cost + 200
    if distane_to_next > how_many_more_miles_cango:
        
        capacity = tank_capacity
        # candidates[0] = (capacity, fuelling_cost)
        candidates.append((capacity, fuelling_cost))

        # must take gas
    else:
        # is double
        if remaining_galon < (tank_capacity / 2):
            # must take gas
            
            capacity = tank_capacity
            # candidates[0] = (capacity, fuelling_cost)
            candidates.append((capacity, fuelling_cost))
        else:
            # now we can either take gas or not
            # choice 1, take gas, chice 2, no gas
            # unless we are at the last stop
            # at that point no need to take gas
            if k != n:
                # add first choice
                capacity = tank_capacity
                candidates.append((capacity, fuelling_cost))

                # add 2nd choice
                fuelling_cost = 0
                capacity = remaining_galon
                candidates.append((capacity, fuelling_cost))
            else:

                fuelling_cost = 0
                capacity = tank_capacity
                candidates.append((capacity, fuelling_cost))
    return candidates




def backtrack(a, k, n, last_point):
    # print ""
    if is_a_solution(a, k, n):
        process_solution(a,k,n)
    else:
        k = k + 1
        candidates = construct_candidates(a, k, n, last_point)
        for can in candidates:
            a[k -1] = can
            backtrack(a, k, n, stations[k-1][0])


backtrack(a, 0, 6, 0)
print min(all_costs)
