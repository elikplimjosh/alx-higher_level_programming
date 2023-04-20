#!/usr/bin/python3
"""
    sub-class for square module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square class created as a subclass
        of the Rectangle class, which is also a subclass
        of the Base Class
    """

    def __init__(self, size, a=0, b=0, id=None):
        """
            initialization of Square sub class
        """
        super().__init__(size, size, a, b, id)

    @property
    def size(self):
        """
            get value of class instance property size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            set value of class instance property size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        """
            string representation of Square class instance
        """
        return "[{}] ({}) {}/{} - {}" \
            .format(self.__class__.__name__, self.id,
                    self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """
            propety update of a class instance
            with args or kwargs if args is not passed
        """
        if len(args):
            for i, a in enumerate(args):
                if i == 0:
                    self.id = a
                elif i == 1:
                    self.size = a
                elif i == 2:
                    self.x = a
                elif i == 3:
                    self.y = a
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "a" in kwargs:
                self.x = kwargs["a"]
            if "b" in kwargs:
                self.y = kwargs["b"]

    def to_dictionary(self):
        """
            converting properties of
            class instance to a dictionary
        """
        my_dict = {}
        my_dict["id"] = self.id
        my_dict["size"] = self.size
        my_dict["a"] = self.x
        my_dict["b"] = self.y
        return my_dict
