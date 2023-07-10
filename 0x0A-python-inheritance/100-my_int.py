#!/usr/bin/python3
# 100-my_int.py
"""class MyInt inheriting from int"""


class MyInt(int):
    """Inheriting from int"""

    def __eq__(self, other):
        """MyInt is a rebel, == behaves like !="""
        return super().__ne__(other)

    def __ne__(sel, other):
        """MyInt is a rebel, != behaves like =="""
        return super().__eq__(other)
