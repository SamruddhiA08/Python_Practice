# math module function
import math


radius = float(input('enter radius'))

circumference = 2*math.pi*radius
area = math.pi*pow(radius,2)
print (f"circumference = {round(circumference)} area = {round(area)}")
