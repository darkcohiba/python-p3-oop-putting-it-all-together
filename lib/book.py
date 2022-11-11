#!/usr/bin/env python3

class Book:
    def __init__(self, title):
        self.title = title
        self.author = ""
        self.page_count = 0
        self.genre = ""
    
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


# FAILED Book in book.py gets initialized with a title. - TypeError: Book() takes no arguments
# FAILED Book in book.py has the title passed into __init__. - TypeError: Book() takes no arguments
# FAILED Book in book.py can be assigned an author name. - TypeError: Book() takes no arguments
# FAILED Book in book.py can be assigned a page count. - TypeError: Book() takes no arguments
# FAILED Book in book.py can be assigned a genre. - TypeError: Book() takes no arguments
# FAILED Book in book.py outputs "Flipping the page...wow, you read fast!" when method turn_page() is called - TypeError: Book() takes no arguments
