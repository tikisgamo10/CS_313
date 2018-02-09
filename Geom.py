# File: Geom.py
#Description: Represent attributes of common geometric figures as well as answer basic questions about them
#Student's Name: Luis Jimenez
#Student's UT EID: laj987
#Partner's Name: N/A
#Partner's UT EID: N/A
#Course Name: CS 313E
#Unique Number: 51335
#Date Created: January 31st 10:44AM
#Date Last Modified: February 1st 5:38PM


import math

class Point (object):
  # constructor
    def __init__ (self, x = 0, y = 0):
        self.x = x
        self.y = y

  # get the distance
    def dist (self, other):
        return math.hypot (self.x - other.x, self.y - other.y)

  # get a string representation of Point
    def __str__ (self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # test the equality of two Points
    def __eq__ (self, other):
        tol = 1.0e-16
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
    def __init__ (self, radius = 1, x = 0, y = 0):
        self.radius = radius
        self.center = Point (x, y)

  # compute the circumference
    def circumference (self):
        return 2.0 * math.pi * float(self.radius)

  # compute the area
    def area (self):
        return math.pi * float(self.radius) * float(self.radius)

  # determine if a point is strictly inside the circle
    def point_inside (self, p):
        return (self.center.dist(p) < self.radius)

  # determine if a circle is inside this circle
    def circle_inside (self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

  # determince if a circle, c, intersects this circle
    def does_intersect (self, c):
        distance = self.center.dist(c.center)
        return (distance < (self.radius + c.radius))

    def circle_circumscribes(self, r):
        x = r.ul.x + (r.length() / 2)
        y = r.lr.y + (r.width() / 2)
        radius = (r.ul.dist(r.lr))/2
        circle = Circle(radius, x, y)
        return circle
    
    def __str__ (self):
        return '(' + str(self.center.x) + ', ' + str(self.center.y) + ') : (' + str(self.radius) + ')' 
    
    def __eq__ (self, other):
        tol = 1.0e-16
        return (abs(self.radius - other.radius) < tol)
    
class Rectangle (object):
    def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
        if ((ul_x < lr_x) and (ul_y > lr_y)):
            self.ul = Point (ul_x, ul_y)
            self.lr = Point (lr_x, lr_y)
        else:
            self.ul = Point (0, 1)
            self.lr = Point (1, 0)
    
    def length (self):
        return self.lr.x - self.ul.x
    
    def width (self):
        return self.ul.y - self.lr.y
    
    def perimeter (self):
        return (2*self.length()) + (2*self.width())
    
    def area(self):
        return (self.length()) * (self.width())
    
    def point_inside (self, p):
        return (p.x < self.lr.x) and (p.x > self.ul.x) and (p.y < self.ul.y) and (p.y > self.lr.y)
    
    def rectangle_inside(self, r):
        #Since all rectangles are assumed to have their base and height parallel to the 
        #x-axis and y-axis, respectively, then if the upper left and lower right corners of
        #another rectangle are strictly inside this rectangle, then the other rectangle MUST
        #be strictly inside this rectangle
        return (self.point_inside(r.ul)) and (self.point_inside(r.lr))
    
    def does_intersect(self, other):
        #Because we are assuming that every rectangle in our program has its base parallel to the x-axis and its height parallel to the y-axis then we have
        #that every rectangle in our program is entirely equivalent to the cartesian product (ul.x, lr.x) x (lr.y, ul.y), i.e. the cartesian product  
        #of the interval between the x-coordinate of the left side and the x-axis of the right side of the rectangle times the interval between the
        #y-coordinate of the bottom side of the rectangle and the y-coordinate of the rectangle
        #It follows that two rectangles intersect if and only if their cartesian product intersect. This is the method used in the following code
        
        #Checks if the x-interval in the cartesian products overlaps
        x_interval_intersects = False
        
        if(other.lr.x >= self.lr.x):
            if(other.ul.x < self.lr.x):
                x_interval_intersects = True
        else:
            if(self.ul.x < other.lr.x):
                x_interval_intersects = True
                
        #Checks if y-interval in cartesian product overlaps        
        y_interval_intersects = False
        
        if(other.ul.y >= self.ul.y):
            if(other.lr.y < self.ul.y):
                y_interval_intersects = True
        else:
            if(self.lr.y < other.ul.y):
                y_interval_intersects = True
                
        #rectangles overlap if and only if both intervals intersect
        return (x_interval_intersects and y_interval_intersects)    
    
    def rect_circumscribe (self, c):
        ul_x = c.center.x - c.radius
        ul_y = c.center.y + c.radius
        lr_x = c.center.x + c.radius
        lr_y = c.center.y - c.radius
        return Rectangle(ul_x, ul_y, lr_x, lr_y)
    
    def __str__ (self):
        return "(" + str(self.ul.x) + ", " + str(self.ul.y) + ") : (" + str(self.lr.x) + ", " + str(self.lr.y) + ") "
    
    def __eq__ (self, other):
        tol = 1.0e-16
        return (abs(self.length() - other.length()) < tol) and (abs(self.width() - other.width()) < tol)
        
        
    
    
def main():
    geom_file_input = open('geom.txt', 'r')
    
    #Get point P
    p_coordinates = geom_file_input.readline().strip().split(" ")
    p = Point(float(p_coordinates[0]), float(p_coordinates[1]))
    
    #Get point Q
    q_coordinates = geom_file_input.readline().strip().split(" ")
    q = Point(float(q_coordinates[0]), float(q_coordinates[1]))
    
    #Get circle C
    c_info = geom_file_input.readline().strip().split(" ")
    c = Circle(float(c_info[2]) , float(c_info[0]), float(c_info[1]))

    #Get circle D
    d_info = geom_file_input.readline().strip().split(" ")
    d = Circle(float(d_info[2]) , float(d_info[0]), float(d_info[1]))
    
    #Get rectangle G
    g_coordinates = geom_file_input.readline().strip().split(" ")
    g = Rectangle(float(g_coordinates[0]), float(g_coordinates[1]), float(g_coordinates[2]), float(g_coordinates[3]))
    
    #Get rectangle H
    h_coordinates = geom_file_input.readline().strip().split(" ")
    h = Rectangle(float(h_coordinates[0]), float(h_coordinates[1]), float(h_coordinates[2]), float(h_coordinates[3]))
    
    print(" ")
    print("Coordinates of P: " + str(p))
    print("Coordinates of Q: " + str(q))
    print("Distance between P and Q: " + "{0:.2f}".format(p.dist(q)))
    print("Circle C: " + str(c))
    print("Circle D: " + str(d))
    print("Circumference of C: " + "{0:.2f}".format(c.circumference()))
    print("Area of D: " + "{0:.2f}".format(d.area()))
    if(c.point_inside(p)):
        print("P is inside C")
    else:
        print("P is not inside C")
        
    if(d.circle_inside(c)):
        print("C is inside of D")
    else:
        print("C is not inside D ")
        
    if(d.does_intersect(c)):
        print("C does intersect D")
    else:
        print("C does not intersect D ")
        
    if(c == d):
        print("C is equal to D")
    else:
        print("C is not equal D")
    
    print("Rectangle G: " + str(g))
    print("Rectangle H: " + str(h))
    print("Length of G: " + str(g.length()))
    print("Width of H: " + str(h.width()))
    print("Perimeter of G: " + str(g.perimeter()))
    print("Area of H: " + "{0:.2f}".format(h.area()))
    if(g.point_inside(p)):
        print("P is inside G")
    else:
        print("P is not inside G")
    
    if(h.rectangle_inside(g)):
        print("G is inside H")
    else:
        print("G is not inside H")
        
    if(h.does_intersect(g)):
        print("G does overlap H")
    else:
        print("G does not overlap H")
        
    print("Circle that circumscribes G: " + str(Circle().circle_circumscribes(g)))
    print("Rectangle that circumscribes D: " + str(Rectangle().rect_circumscribe(d)))
    if(g == h):
        print("Rectangle G is equal to H")
    else:
        print("Rectangle G is not equal to H")
    
    
    print(" ")

main()
