import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("lightgreen")
t.pensize(2)

# EXERCİSE 1

# def fizz_buzz(n):
#   for n in range(1,n+1):
#     if n % 3 == 0 and n % 5 == 0:
#         print('FizzBuzz')
#     elif n % 3 == 0:
#         print ('Fizz')
#     elif n % 5 == 0:
#         print ('Buzz')
#     else :
#         print (n)
#
# fizz_buzz(20)

# EXERCİSE 2

# def digit_sum(n):
#     sum = 0
#     while n > 0 :
#         sum = sum + n % 10
#         n = n // 10
#     return sum
#
# print (digit_sum(1234))

# EXERCİSE 3

# def  alternate_case(s):
#     new = ""
#     for i in range (len(s)):
#         if i % 2 == 0:
#             new = new + s[i].upper()
#         else :
#             new = new + s[i].lower()
#     return new
#
# print(alternate_case("hello world"))

# EXERCİSE 4

# def draw_polygon(t, sides, length):
#     for i in range(sides):
#         t.fd(length)
#         t.left(360/sides)
#
# list_of_figures = [(3 , "red" ,(-150, -30)), (4 , "yellow" ,(-30, -30)), (5 , "blue" ,(90, -30) ) ]
#
# for side,color,location in list_of_figures:
#     t.penup()
#     t.goto(location)
#     t.pendown()
#     t.pencolor(color)
#     draw_polygon(t,side,60)
#
#
# wn.exitonclick()


# EXERCİSE 5

# def filled_square(t, size, color):
#     t.fillcolor(color)
#     t.begin_fill()
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
#     t.end_fill()
# t.penup()
# t.goto(-165,-25)
# t.pendown()
#
# colors = ["red", "blue", "red", "blue" , "red"  ]
# for c in colors:
#     filled_square(t, 40, c)
#     t.penup()
#     t.forward(70)
#     t.pendown()
#
# wn.exitonclick()

# Exercise 6

# def draw_spuare(t,size):
#     for i in range(4):
#      t.forward(size)
#      t.left(90)
#
# for i in range(12):
#     draw_spuare(t,80)
#     t.left(30)
#
# wn.exitonclick()

# Exercise 7

def draw_spuare(t , fill ):
    if fill :
        t.color("black")
        t.begin_fill()
    for _ in range(4):
        t.forward(40)
        t.left(90)
    if fill :
        t.end_fill()

for row in range(6):
    for col in range(6):
        x = -120 + (col * 40)
        y= -120 + (row * 40)
        t.penup()
        t.goto(x,y)
        t.pendown()
        should_fill = (row + col) % 2 == 0

        draw_spuare(t, should_fill)

wn.exitonclick()
