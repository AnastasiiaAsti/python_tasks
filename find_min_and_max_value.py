# Your task is to make two functions ( max and min, or maximum and minimum, etc.,
# depending on the language ) that receive a list of integers as input,
# and return the largest and lowest number in that list, respectively.

def minimum(arr):
    return min(arr)


def maximum(arr):
    return max(arr)

# option 2


def min(arr):
    low = arr[0]
    for i in arr[1:]:
        if i < low:
            low = i
    return low


def max(arr):
    high = arr[0]
    for i in arr[1:]:
        if i > high:
            high = i
    return high
