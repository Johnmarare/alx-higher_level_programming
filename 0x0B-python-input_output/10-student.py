#!/usr/bin/python3
# 10-student.py
"""student to json with filter"""


class Student:
    """student to JSON with filter"""

    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation
        Args:
            attrs (any): attributes
        Returns:
            dictionary representation
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
