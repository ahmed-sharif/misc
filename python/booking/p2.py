# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations 
import math
from math import acos, sin, cos

def distance_between(point1, point2):

    EARTH_RADIUS = 6371  # ;//in km
    point1_lat_in_radians  = math.radians( float(point1[0])  )
    point2_lat_in_radians  = math.radians( float(point2[0])  );
    point1_long_in_radians  = math.radians( float(point1[1])  );
    point2_long_in_radians  = math.radians( float(point2[1])  );

    return acos( sin( point1_lat_in_radians ) * sin( point2_lat_in_radians ) +
                 cos( point1_lat_in_radians ) * cos( point2_lat_in_radians ) *
                 cos( point2_long_in_radians - point1_long_in_radians) ) * EARTH_RADIUS;





no_guest = int(raw_input().strip())

guest_interest = []

for _ in range(no_guest):
    inte = raw_input().strip().split()
    guest_interest.extend(inte[1:])

city_info = {}
no_of_city = int(raw_input().strip())

for _ in range(no_of_city):
    city = raw_input().strip().split()
    city_name = city[0]
    city_lat = city[1]
    city_long = city[2]
    attractions = city[4:]
    city_info[city_name] = [city_name, city_lat, city_long, attractions]
# print city_info
matches = {}   
g_set = set(guest_interest)   
# print g_set
for cities in combinations(city_info.keys(), 2):
    print cities
    s1 = set(city_info[cities[0]][3])
    print s1
    s2 = set(city_info[cities[1]][3])
    print s2
    s3 = s1.union(s2)
    print s3
    s4 = s3.intersection(g_set)
    print s4
    matches[cities] = len(s4)

max_match = max(matches.values())

new_match_dict = {}

for cities, attrs in matches.items():
    if attrs == max_match:
        new_match_dict[cities] = attrs


distances = {}


if len(new_match_dict.keys()) > 1:
    print "choices"
    print new_match_dict
    # print new_match_dict
    for x in new_match_dict:
        distances[x] = distance_between([city_info[x[0]][1],city_info[x[0]][2]], [city_info[x[1]][1],city_info[x[1]][2]])
    m_distance = min(distances.values())
    print distances
    for x, dis in distances.items():
        if dis == m_distance:
            t1 = list(x)
            t1.sort()
            print "result"
            print " ".join(t1)
            break

else:
    # print new_match_dict
    # t1 = list(new_match_dict[new_match_dict.keys()[0]])
    t1 = list(new_match_dict.keys()[0])
    t1.sort()
    print "result"
    print " ".join(t1)
        
    
    
    
    



    
    

    

    
