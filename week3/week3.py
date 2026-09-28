# EXERCISE1

height=float(input("height: "))
width=float(input("width: "))

area=height*width

print("area=",area)


# EXERCISE2

galon = float(input("Galon : "))
miles = float(input("Miles : "))

mpg = miles / galon
print(f"Miles: {mpg}")

# EXERCISE3

fahrenheit =float(input("Enter a temperature in Fahrenheit: "))
degrees = (fahrenheit-32)/1.8
print(degrees)

# EXERCISE4

Starting_Day = int(input("Enter starting day (0 = Sunday, 1 =Monday, …, 6 = Saturday): "))
lentgh_of_vacation = int(input("enter length of vacation: "))

total = (lentgh_of_vacation + Starting_Day)
end_day = total%7

print(end_day)

# EXERCISE5
import math
the_radius_of_the_circle=float(input("Enter the radius of the circle: "))
π = float( 3.14 )
circumference = 2*the_radius_of_the_circle*math.pi

print("The circumference of the circle is:", circumference)

# EXERCISE6

birth_year = int(input("Enter birth year: "))
age = 2026 - birth_year
print(age)

# EXERCISE7

import turtle
t = turtle.Turtle()
while True:
        t.color("green")
        t.forward(100)
        t.left(90)
        t.speed(2)
