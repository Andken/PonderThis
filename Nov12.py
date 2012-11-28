#!/usr/bin/python

#Ponder This Challenge:
#Thanks to Adir Pridor for the following challenge:
#A gardener plants a tree on every integer lattice point, except the origin, inside a circle with a radius of 9801. The trees are cylindrical in shape and all grow together at the same rate.
#As the trees grow, more and more points outside the circle of trees stop having a direct line of sight with the origin. What will be the trees' radius when the origin first loses its line of sight with all the points outside the circle? Please give your answer as a decimal number with an accuracy of 13 digits (13 significant digits).
#Here is a sketch of a forest of radius 5 and a light beam entering the origin (center of the forest).


import math

RADIUS = 5
RADIUS = 9801
EPSILON = 0.00000000000001

def distance(m, x0, y0):
    return abs(m*x0-y0)/math.sqrt(m**2+1)

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

# need to find the smallest positive number
point1 = points[diff.index(min(diff))]
XX = [v<0 for v in diff]
XX2 = [RADIUS*v2 for v2 in XX]
XX3 = [v3+v4 for v3, v4 in zip(diff, XX2)]
#print XX
#print XX2
#print XX3
point2 = points[XX3.index(min(XX3))]
print point1, point2
