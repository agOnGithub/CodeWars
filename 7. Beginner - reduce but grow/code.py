def grow(arr):
    res = 1
    i = 0
    while i < len(arr):
        res *= arr[i]
        i += 1
    return res