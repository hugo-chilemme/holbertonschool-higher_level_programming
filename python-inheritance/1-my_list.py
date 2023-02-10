#!/usr/bin/python3
"""MyList"""


class MyList(list):
    """MyList"""
    def print_sorted(self):
        json = []
        for element in self.copy():
            if type(element) is int:
                json.append(element)
        print(sorted(json))
