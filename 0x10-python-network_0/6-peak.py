#!/usr/bin/python3


def find_peak(list_of_integers):
    """
    Find the Peaks within the list of unsorted Integer

    Args:
        list_of_integers (list): A list of unsorted Integers

    Returns:
        int or None
    """
    if not list_of_integers:
        return None
    else:
        peaKnum = list_of_integers[0]
        length = len(list_of_integers)
        for i in range(length - 1):
            if list_of_integers[i] > list_of_integers[i + 1]:
                peaKnum = list_of_integers[i]
    return peaKnum
