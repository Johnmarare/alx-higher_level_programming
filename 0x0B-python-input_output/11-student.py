#!/usr/bin/python3
# 11-student.py
"""student to disk reload"""


class Student:
    """defines a student by name and age"""

    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation"""
        if (type(attrs) == list and
                all(type(ele) == str for ele in atrrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return (self.__dict__)

    def reload_from_json(self, json):
        """Replaces all atributes of student instance"""
        for key, value in json.items():
            setattr(self, key, value)
