# EXERCİSE1
# import math

# import random
# for i in range(10):
#     print (random.random())

# EXERCİSE2

# import random
# for i in range(10):
#    print(random.randint(25,35))

# EXERCİSE3
# 1.
# import math
# a=3
# b=4
# c=math.hypot(a,b)
# print (c)

# 2.
# a=int(input("enter a:"))
# b=int(input("enter b:"))
#
# c=math.sqrt(a**2+b**2)
# print(c)

# EXERCİSE4

# import math
#
# def areaOfCircle(r):
#     return math.pi * r**2
#
# print(areaOfCircle(int(input("Enter the radius of the circle: "))) )

# EXERCİSE5

# import turtle
#
# def drawstar(t,side):
#     for i in range(5):
#         t.forward(side)
#         t.right(144)
#
# turt=turtle.Turtle()
# screen=turtle.Screen()
# drawstar(turt,100)
#
# screen.exitonclick()

# EXERCİSE6

# import turtle
#
# def drawSquare(t, size):
#     for _ in range(4):
#          t.forward(size)
#          t.left(90)
#
# wn = turtle.Screen()
# wn.bgcolor("green")
#
# alex=turtle.Turtle()
# alex.color("pink")
# alex.pensize(3)
#
# for _ in range(5):
#     drawSquare(alex, 20)
#     alex.penup()
#     alex.forward(40)
#     alex.pendown()
#
# wn.exitonclick()

#

# EXERCİSE7

# import turtle
# def drawSquare(t,sz):
#     for _ in range(4):
#         t.forward(sz)
#         t.left(90)
#         t.forward(sz)
#         t.left(90)
#
# wn=turtle.Screen()
# wn.bgcolor("lightgreen")
#
# alex=turtle.Turtle()
# alex.color("pink")
# alex.pensize(3)
#
# size = 20
# for i in range(5):
#     drawSquare(alex,size)
#     size += 20
#     alex.penup()
#     alex.goto(alex.xcor()-10,alex.ycor()-10)
#     alex.pendown()



