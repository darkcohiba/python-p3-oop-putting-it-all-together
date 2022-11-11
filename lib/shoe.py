#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand):
        self.brand = brand
        self.color = ""
        self.size = 0
        self.material = ""
        self.condition = "old"
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
    


# FAILED Shoe in shoe.py gets initialized with a brand. - TypeError: Shoe() takes no arguments
# FAILED Shoe in shoe.py has the brand passed to __init__. - TypeError: Shoe() takes no arguments
# FAILED Shoe in shoe.py can be assigned a color. - TypeError: Shoe() takes no arguments
# FAILED Shoe in shoe.py can be assigned a size. - TypeError: Shoe() takes no arguments
# FAILED Shoe in shoe.py can be assigned a material. - TypeError: Shoe() takes no arguments
# FAILED Shoe in shoe.py can be assigned a condition. - TypeError: Shoe() takes no arguments
# FAILED Shoe in shoe.py says that the shoe has been repaired. - TypeError: Shoe() takes no arguments
# FAILED Shoe in shoe.py has "New" condition after repair. - TypeError: Shoe() takes no arguments