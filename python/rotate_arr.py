



arr = [1, 2, 3, 4, 5, 6, 7]


def rotate(arr, k):

    k = k % len(arr)

    new_arr = arr[k:]
    new_arr.extend(arr[:k])
    return new_arr

def rotate_right(arr, k):
    new_arr = arr[-k:]
    new_arr.extend(arr[:-k])
    return new_arr

