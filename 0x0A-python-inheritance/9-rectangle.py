#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
     class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
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
        class Rectangle that inherits from BaseGeometry
        """
        return self.__width * self.__height
