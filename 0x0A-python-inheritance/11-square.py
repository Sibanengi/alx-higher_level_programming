#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square that inherits from Rectangle
    """

    def __init__(self, size):
        """
        constructor of class Square
        """
        self.__size = size

    def area(self):
        """
        Area of the Square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        define str print a string unofficial
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
