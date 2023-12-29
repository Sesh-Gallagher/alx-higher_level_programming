#!/usr/bin/python3


import sys


def safe_function(fct, *args):
    try:

        retrn = fct(*args)
        return (retrn)
    except Exception as i:
        print("Exception: {}".format(i), file=sys.stderr)
        return None
