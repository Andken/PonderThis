#!/usr/bin/python

#Ponder This Challenge:
#Thanks to Adir Pridor for the following challenge:
#A gardener plants a tree on every integer lattice point, except the origin, inside a circle with a radius of 9801. The trees are cylindrical in shape and all grow together at the same rate.
#As the trees grow, more and more points outside the circle of trees stop having a direct line of sight with the origin. What will be the trees' radius when the origin first loses its line of sight with all the points outside the circle? Please give your answer as a decimal number with an accuracy of 13 digits (13 significant digits).
#Here is a sketch of a forest of radius 5 and a light beam entering the origin (center of the forest).


# there are 98 gaps to consider between y=0&1, y=1&2, y=2&3, etc.

# 1st gap ... figure out x position of tree with largest x where y = 1
# x**2 + y**2 = 9801
x = int((9800)**0.5)

# limiting factor is (1,0) and (98,1)

# y = mx+b
# y' = radius of tree
# y' = m*1+0
# 1-y' = m*98 + 0
# y' = 1/99.
y_prime = 1/99.
m = y_prime

# 2nd gap:
# limiting factor is (97,1) and (98,1)
# 1-y' = m * 97
# 1+y' = m * 98
y_prime = max(y_prime, 1/195.)

# how to determine limiting factors for each gap
# sweep the line across gap and find maximum distance from each integer vertex

