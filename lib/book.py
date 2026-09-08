#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        # Set the book title and page count
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Check that page count is an integer
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        # Print a message when the page is turned
        print("Flipping the page...wow, you read fast!")
        