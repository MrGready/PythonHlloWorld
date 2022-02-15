'''import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    new_color = (r, g, b)
    rgb_colors.append(color.rgb)

print(rgb_colors)'''

import turtle as t
import random

tim = t
tim.colormode(255)
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
              (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
tim.hideturtle()


def draw_dot(space, x):
    for i in range(x):
        for j in range(x):
            tim.color(random.choice(color_list))
            tim.dot(10)

            tim.forward(space)
        tim.backward(space * x)

        tim.left(90)
        tim.forward(space)
        tim.right(90)


tim.penup()
draw_dot(30, 10)
