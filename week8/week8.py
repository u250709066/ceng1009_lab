# def getGrade(mark):
#     if mark >= 90:
#         return "A"
#     elif mark >= 80:
#         return "B"
#     elif mark >= 70:
#         return "C"
#     elif mark >= 60:
#         return "D"
#     else:
#         return "F"
#
# marks = [95,90,89.9,85,80,79,9,75,70,65,60,59,9,0]
# for mark in marks:
#       print("your grade is ", getGrade(mark))
#
# EXERCİSE 2
# import turtle
# screen = turtle.Screen()
# t=turtle.Turtle()
#
# def chooseColor(height):
#
#     if height >= 200:
#         return "red"
#     if height >= 100 < 200:
#         return "yellow"
#     if height <= 100 :
#         return "green"
#
#
#
# def drawBar(t , height, gap):
#     t.penup()
#     t.left(90)
#     t.forward(height + gap)
#     t.write("" + str(height))
#     t.backward(height + gap)
#     t.right(90)
#     t.pendown()
#
#     t.begin_fill()
#     t.fillcolor(chooseColor(height))
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barChart(data):
#     maxheight = max(data)
#     num_bars = len(data)
#
#     border = 10
#     gap = (maxheight + border) / 25
#
#     screen.bgcolor("lightgreen")
#     right = 40 * num_bars + border
#     top = maxheight + 4 * gap
#     screen.setworldcoordinates(-border , -border , right , top)
#
#     t.color("blue")
#
#     t.pensize(3)
#
#     for height in data:
#         drawBar(t, height, gap)
#
#
#
# data = [48, 117, 200, 240, 160, 260, 220]
# barChart(data)

# screen.exitonclick()


# import turtle
# screen = turtle.Screen()
# t=turtle.Turtle()
#
# def chooseColor(height):
#
#     if height >= 200:
#         return "red"
#     if height >= 100 < 200:
#         return "yellow"
#     if height <= 100 :
#         return "green"
#
# def drawBar(t , height, gap):
#     if height >= 0:
#         labelY = height + gap
#     else:
#         labelY = gap
#     t.penup()
#     t.left(90)
#     t.forward(height + gap)
#     t.write("" + str(height))
#     t.backward(height + gap)
#     t.right(90)
#     t.pendown()
#
#     t.begin_fill()
#     t.fillcolor(chooseColor(height))
#     t.left(90)
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barChart(data):
#     maxheight = max(data)
#     min_height = min(data)
#     border = 10
#     bottom = min(min_height, maxheight)
#     num_bars = len(data)
#
#     border = 10
#     gap = (maxheight + border) / 25
#
#     screen.bgcolor("lightgreen")
#     right = 40 * num_bars + border
#     top = maxheight + 4 * gap
#     screen.setworldcoordinates(-border , bottom , right , top)
#
#     t.color("blue")
#
#     t.pensize(3)
#
#     for height in data:
#         drawBar(t, height, gap)
#
#
#
# data = [48, 117, 200, 240, 160, 260, 220 , -20 , -123]
# barChart(data)





# EXERCİSE_4
import math
# def findHypot(side1,side2):
#     return math.sqrt(side1**2+side2**2)
# def findHypot(side1,side2):
#     return (side1**2+side2**2)**0.5
# print(findHypot(3,4))