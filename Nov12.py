#!/usr/bin/python

#Ponder This Challenge:
#Thanks to Adir Pridor for the following challenge:
#A gardener plants a tree on every integer lattice point, except the origin, inside a circle with a radius of 9801. The trees are cylindrical in shape and all grow together at the same rate.
#As the trees grow, more and more points outside the circle of trees stop having a direct line of sight with the origin. What will be the trees' radius when the origin first loses its line of sight with all the points outside the circle? Please give your answer as a decimal number with an accuracy of 13 digits (13 significant digits).
#Here is a sketch of a forest of radius 5 and a light beam entering the origin (center of the forest).


import math
import operator

RADIUS = 5
#RADIUS = 9801
EPSILON = 0.00000000000001



def distance(m, p):
    return abs(m*p[0]-p[1])/math.sqrt(m**2+1)

def circle_intercept(m):
    x = math.sqrt(RADIUS**2/(m**2+1))
    y = m*x
    return (x,y)

def points_of_interest(m):
    poi = []
    (x0,y0) = circle_intercept(m)
    for x in range(1, int(x0+1)):    
        y = m*x
        if(x**2 + int(round(y))**2 <= RADIUS**2):
            poi.append((x, int(round(y))))

        if(x**2 + int(round(y+1))**2 <= RADIUS**2):
            poi.append((x, int(round(y+1))))

    return poi

def max_tree_radius_slope(p0, p1):
    return (float(p0[1])-float(p1[1]))/(float(p0[0])-float(p1[0]))

def max_tree_radius(p0, p1):
    m = max_tree_radius_slope(p0, p1)
    print m, p0, distance(m, p0)
    print m, p1, distance(m, p1)
    return distance(m, p1)


m = 0.0
points = points_of_interest(m)
orig = [abs(m*p[0]-p[1])/math.sqrt(m**2+1) for p in points]
m=m+EPSILON
adjust = [abs(m*p[0]-p[1])/math.sqrt(m**2+1) for p in points]
diff = [a-o for a, o in zip(adjust, orig)]
#print orig
#print adjust
#print diff
#print points

min_index, min_value = min(enumerate(diff), key=operator.itemgetter(1))
point1 = points[min_index]


# need to find the smallest positive number
min_index, min_value = min(enumerate([(RADIUS*(v<0))+v for v in diff]), key=operator.itemgetter(1))
point2 = points[min_index]
print point1, point2
print max_tree_radius(point1, point2)

