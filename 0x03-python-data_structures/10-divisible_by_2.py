#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    divised_list = []
    for a in range(len(my_list)):
        if my_list[a] % 2 == 0:
            divised_list.append(True)
        else:
            divised_list.append(False)

    return (divised_list)
