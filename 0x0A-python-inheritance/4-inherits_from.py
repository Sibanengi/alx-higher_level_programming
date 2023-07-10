#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Function checks if an object is an instance of a class that
    inherited (directly or indirectly) from specified class
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
