#!/usr/bin/python3

from sys import stderr


def safe_function(fct, *args):

    try:
        result = fct(*args)
    except Exception as e:
        stderr.write("Exception: {}\n".format(e))
        return (None)
    return (result)
