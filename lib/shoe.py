#!/usr/bin/env python3

class Shoe:
    def __init__(self,brand,color = "",size = "", condition = ""):
        self.brand = brand
        self.color = color
        self._size = size
        self.condition = condition
    
    def set_color(self,color):
        self._color = color
    def get_color(self):
        return self._color
    def set_size(self,size):
        if(type(size) is not int):
            print("size must be an integer")
        else:
            self._size = size
    def get_size(self):
        return self._size
    
    def set_brand(self,brand):
        self.brand = brand
    def get_brand(self):
        return self.brand

    def set_condition(self,condition):
        self.condition = condition
    def get_condition(self):
        return self.condition

    def cobble(self):
        self.set_condition("New")
        print("Your shoe is as good as new!")
        
    size = property(get_size, set_size,)
