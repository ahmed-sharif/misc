# remove duplicates from a sorted array

def remove_dups(arr):
    last_valid_position = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[last_valid_position-1]:
            arr[last_valid_position] = arr[i]
            last_valid_position += 1

    return last_valid_position, arr[:last_valid_position]

print remove_dups([1,2,2,3,4,5,5,6,7])
print remove_dups([1,2,3,4,5,6,7,8,8])
print remove_dups([1,1,3,4,5,6,7,8,8])
print remove_dups([1,1,3,4,5,5,7,8,8])

"""

1   2   2   3   4   4   4   5

    i
    l
        i
        l
            i
        l
                i
            l
"""
