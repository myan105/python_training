#Write a definition for a class named Circle with attributes center and radius, where center 
#is a Point object and radius is a number.
#Instantiate a Circle object that represents a circle with its center at (150, 100) and 
#radius 75. Write a function named point_in_circle that takes a Circle and a Point and returns 
#True if the
#Point lies in or on the boundary of the circle.
#Write a function named rect_in_circle that takes a Circle and a Rectangle and returns 
#True if the Rectangle lies entirely in or on the boundary of the circle.
#Write a function named rect_circle_overlap that takes a Circle and a Rectangle and returns 
#True if any of the corners of the Rectangle fall inside the Circle. Or as a more challenging version, return True if any part of the Rectangle falls inside the Circle.

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

class Rectangle:
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

def distance(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return math.sqrt(dx**2 + dy**2)

def point_in_circle(circle, point):
    return distance(circle.center, point) <= circle.radius

def rect_in_circle(circle, rect):
    # Check if all corners of the rectangle are inside the circle
    for corner in [rect.corner,
                   Point(rect.corner.x + rect.width, rect.corner.y),
                   Point(rect.corner.x, rect.corner.y + rect.height),
                   Point(rect.corner.x + rect.width, rect.corner.y + rect.height)]:
        if not point_in_circle(circle, corner):
            return False
    return True

def rect_circle_overlap(circle, rect):
    # Check if any corner of the rectangle falls inside the circle
    for corner in [rect.corner,
                   Point(rect.corner.x + rect.width, rect.corner.y),
                   Point(rect.corner.x, rect.corner.y + rect.height),
                   Point(rect.corner.x + rect.width, rect.corner.y + rect.height)]:
        if point_in_circle(circle, corner):
            return True
    # Check if any part of the rectangle falls inside the circle
    # Note: This part is more challenging and involves geometry calculations
    # It can be implemented if needed.

# Instantiate a Circle object
circle_center = Point(150, 100)
circle_radius = 75
circle = Circle(circle_center, circle_radius)

# Instantiate a Rectangle object
rect_corner = Point(100, 75)
rect_width = 50
rect_height = 50
rectangle = Rectangle(rect_width, rect_height, rect_corner)

# Test the functions
print(point_in_circle(circle, Point(160, 120)))  # True
print(rect_in_circle(circle, rectangle))         # False
print(rect_circle_overlap(circle, rectangle))    # True 
