#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers"""

def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """

    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size  == 0:
        return (None)
    elif size == 1:
        return (list_of_integers[0])
    elif size == 1:
        return max(list_of_integers)

    mid = int(size/2)
    peak = list_of_integers[mid]
    mylist = list_of_integers
    if peak > mylist[mid - 1] and peak > mylist[mid + 1]:
        return peak
    elif peak < mylist[mid - 1]:
        return find_peak(mylist[:mid])
    else:
        return find_peak(mylist[mid + 1:])
