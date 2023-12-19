#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new_list = 0
    div = []

    for x in range(0, list_length):
        try:

            new_list = my_list_1[x] / my_list_2[x]
        except TypeError:
            new_list = 0
            print("wrong type")

        except ZeroDivisionError:
            new_list = 0
            print("division by 0")

        except IndexError:
            new_list = 0
            print("out of range")

        finally:
            pass
        div.append(new_list)

        return (div)
