import turtle

import colorgram
import random

from turtle import Turtle

turtle.colormode(255)

tim = Turtle()
extracted_color=colorgram.extract('hirst.jpg', 30)
rgb_color=[]
for color in extracted_color:
    r=color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    new_color=(r,g,b)
    rgb_color.append(new_color)
print(rgb_color)
# [ (241, 242, 47), (177, 173, 8),
# (239, 57, 213), (36, 180, 10), (158, 4, 90), (235, 48, 10), (212, 8, 4), (59, 145, 241), (67, 4, 146),
# (89, 239, 248), (244, 53, 17), (221, 138, 63), (234, 214, 2), (118, 232, 208), (216, 121, 200), (172, 52, 108),
# (60, 133, 224), (43, 157, 24), (119, 196, 98),
# (239, 161, 220), (52, 7, 108), (243, 167, 155), (251, 6, 10), (96, 77, 149), (251, 10, 7), (96, 7, 58)]
# def colors():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     new_color = (r,g,b)
#     return new_color






screen = turtle.Screen()
turtle.exitonclick()
