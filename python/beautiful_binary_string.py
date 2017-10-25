
def find_all(src, pat="010"):
    res = []
    loc = src.find(pat)
    while loc != -1:
        res.append(loc)
        loc = src.find(pat, loc + 2)
    return res


def find_replacement_count(locations):
    ln = len(locations)
    if ln < 2:
        return ln

    count = 1
    found = False
    for i in range(1, len(locations)):
        if locations[i] - locations[i -1] == 2:
            if found == False:
                found = True
            else:
                count += 1
                found = False
        else:
            count += 1
            found = False
    return count


strs = ["0101010", "01010101010", "010101010", "01100", "0100101010"]

for s in strs:
    locations = find_all(s)
    print locations
    print find_replacement_count(locations)

    # count = 1
