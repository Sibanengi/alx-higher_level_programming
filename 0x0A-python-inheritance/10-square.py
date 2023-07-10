#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
     class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        constructor of class Rectangle
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def __str__(self):
        """
        define str print a string unofficial
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Area of Rectangle
        """
        return self.__width * self.__height


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
