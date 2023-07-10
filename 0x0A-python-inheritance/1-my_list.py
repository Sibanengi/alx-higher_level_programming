#!/usr/bin/python3
class MyList(list):
    """
    class MyList that inherits from list
    """
    def print_sorted(self):
        """
        Public instance method: that prints the list,
        but sorted (ascending sort)
        """
        print(sorted(self))
