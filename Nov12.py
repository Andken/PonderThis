#!/usr/bin/python

#Ponder This Challenge:
#Thanks to Adir Pridor for the following challenge:
#A gardener plants a tree on every integer lattice point, except the origin, inside a circle with a radius of 9801. The trees are cylindrical in shape and all grow together at the same rate.
#As the trees grow, more and more points outside the circle of trees stop having a direct line of sight with the origin. What will be the trees' radius when the origin first loses its line of sight with all the points outside the circle? Please give your answer as a decimal number with an accuracy of 13 digits (13 significant digits).
#Here is a sketch of a forest of radius 5 and a light beam entering the origin (center of the forest).


import math
import operator
import sys

RADIUS = 5
RADIUS = 9801
EPSILON = 0.00000000000001

def distance_to_origin(p):
    return math.sqrt(p[0]**2 + p[1]**2)

def distance(m, p):
    return abs(m*p[0]-p[1])/math.sqrt(m**2+1)

def circle_intercept(m):
    x = math.sqrt(RADIUS**2/(m**2+1))
    y = m*x
    return (x,y)

def within_circle(p):
    return p[0]**2 + p[1]**2 <= RADIUS**2

def points_of_interest(m):
    upper_poi = []
    #    lower_poi = []
    (x0,y0) = circle_intercept(m)
    previous_y = 0
    for x in range(1, int(x0+1)):
        y = m*x

        if previous_y+1 < y:
            previous_y = previous_y+1

        if within_circle((x, previous_y+1)):
            upper_poi.append((x, previous_y+1))

        #        if within_circle((x, previous_y)):
        #            lower_poi.append((x, previous_y))
        

    return upper_poi

def max_tree_radius_slope(p0, p1):
    return (float(p0[1])+float(p1[1]))/(float(p0[0])+float(p1[0]))

def max_tree_radius(p0, p1):
    m = max_tree_radius_slope(p0, p1)
    return distance(m, p1)

def lowest_m_point(points):
    m = 1
    p_ret = (0,0)
    for p in points:
        if float(p[1])/float(p[0]) < m:
            m = float(p[1])/float(p[0])
            p_ret = p

    return p_ret

m = 0.0
current_max_radius = 0.0
current_m = 0
point = (1,0)
x = 0
while(m<1):
    upoints = points_of_interest(m)

    next_point = lowest_m_point(upoints)
    print point, next_point, max_tree_radius(point, next_point), current_m

    if max_tree_radius(point, next_point) > current_m:
        current_m = max_tree_radius(point, next_point)

    point = next_point
    m = float(point[1])/float(point[0]) + EPSILON
    
#    print points_of_interest(m)

#    x += 1
#    if x > 2:
#        sys.exit()

#    orig = [abs(m*p[0]-p[1])/math.sqrt(m**2+1) for p in points]
#    m=m+EPSILON
#    adjust = [abs(m*p[0]-p[1])/math.sqrt(m**2+1) for p in points]
#    diff = [a-o for a, o in zip(adjust, orig)]
#
#    min_index, min_value = min(enumerate(diff), key=operator.itemgetter(1))
#    point1 = points[min_index]
#
#    # need to find the smallest positive number
#    min_index, min_value = min(enumerate([(RADIUS*(v<0))+v for v in diff]), key=operator.itemgetter(1))
#    point2 = points[min_index]
#
#    print point1, point2
#    
#    if(max_tree_radius(point1, point2) > current_max_radius):
#        current_max_radius = max_tree_radius(point1, point2)
#        current_m = max_tree_radius_slope(point1, point2)
#
#    m = float(point1[1])/float(point1[0])
#    x+=1
#    if x > 1:
#        sys.exit()
