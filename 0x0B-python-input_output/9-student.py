#!/usr/bin/python3
# 9-student.py
"""Class Student defining a student"""


class Student:
    """class student defining a student"""

    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dict representation of student instance"""
        return (self.__dict__)
