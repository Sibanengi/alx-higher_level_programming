#!/usr/bin/python3
class Square:
    """Write a class Square that defines a square"""
    def __init__(self, size=0):
        """Module __init__ for size square validation"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Method area return the square Area"""
        return(self.__size ** 2)

    @property
    def size(self):
        """Method property of size and return the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Method size_setter atributte evaluate the value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Method my_print print a square"""
        if self.__size == 0:
            print("")
            return
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print("")
