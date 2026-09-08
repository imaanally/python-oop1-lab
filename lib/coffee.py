#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        # Set the coffee size and price
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Check that the size is valid
        if value in ["Small", "Medium", "Large"]:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        # Add a tip to the coffee price
        print("This coffee is great, here’s a tip!")
        self.price = self.price + 1