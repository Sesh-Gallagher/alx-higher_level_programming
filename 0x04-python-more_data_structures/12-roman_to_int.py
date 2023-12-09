#!/usr/bin/python3

def roman_to_int(roman_string):

    if type(roman_string) is not str or roman_string is None:
        return (0)

    rmn_int = 0
    rmn_num = (
            {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000})

    for i in range(len(roman_string)):

        if i > 0 and rmn_num[roman_string[i]] > rmn_num[roman_string[i - 1]]:
            (rmn_int) += rmn_num[roman_string[i]] - 2 * \
                    rmn_num[roman_string[i - 1]]
        else:
            (rmn_int) += rmn_num[roman_string[i]]

    return (rmn_int)
