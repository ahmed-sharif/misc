# given a key remove all occurrence of the key from an array




def remove_key(arr, key):
    last_valid_position = 0
    for i in range(len(arr)):
        if arr[i] != key:
            if i != last_valid_position:
                arr[last_valid_position] = arr[i]
            last_valid_position += 1

    return last_valid_position, arr[:last_valid_position]

print remove_key([1,2,3,4,1,2,3], 10)
print remove_key([1,2,3,4,1,2,3], 1)

