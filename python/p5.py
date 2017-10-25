

"""
n = int(raw_input().strip())

persons = []
for _ in range(n):
    inp = raw_input().strip().split()
    persons.append(inp[2:])


events = []
"""

persons = [
    ["museum", "wine", "bike"],
    ["museum", "flower"],
    ["hike", "bike"]
]

events_description = [
    ["flower"],
    ["museum"],
    ["bike", "wine"]
]

events = [
    "E1","E2","E3"
]

for _ in range(n):
    inp = raw_input().strip().split()
    events.append(inp[1:])


for x in range(len(events)):
    for y in range(x + 1):
        key = events[y+1]
        print key
