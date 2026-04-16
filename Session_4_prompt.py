# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:11:29 2026

@author: arian
"""

class Animal:
    
    
    def __init__(self, arm_len, leg_len, eyes_num, tail, furry):
       self.arm_len = float(arm_len)
       self.leg_len = float(leg_len)
       self.eyes_num = int(eyes_num)
       self.tail = bool(tail)
       self.furry = bool(furry)
        
        
        
        
    def print_characteristics(self):
        print(f"""The Arm length of your animal is {self.arm_len} inches
The Leg length of your animal is {self.leg_len} inches
The number of eyes your animal has is {self.eyes_num}
If your animal has a tail {self.tail}
And if your animal is furry {self.furry}
              """)
        
Cat = Animal(9.5,9.6,2,True,True)
Cat.print_characteristics()


