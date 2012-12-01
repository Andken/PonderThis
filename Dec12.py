#!/usr/bin/python

#Ponder This Challenge:
#36 people live in a 6x6 grid, and each one of them lives in a separate square of the grid. Each resident's neighbors are those who live in the squares that have a common edge with that resident's square.
#Each resident of the grid is assigned a natural number N, such that if a person receives some N>1, then he or she must also have neighbors that have been assigned all of the numbers 1,2,...,N-1.
#Find a configuration of the 36 neighbors where the sum of their numbers is at least 90.
#Finding a sum of more than 90 will earn you a star near your name.
#As an example, the highest sum we can get in a 3x3 grid is 20:
#1 2 1
#4 3 4
#2 1 2

import random
import sys

N=6
SUM=90
FIVE_SET = set([1,2,3,4])
FOUR_SET = set([1,2,3])
THREE_SET = set([1,2])

def isGood(grid):
    for x in range(N):
        for y in range(N):
            if not checkIndex(grid, x, y):
                return False
    return True

def checkIndex(grid, x, y):
    X = []
    X.append(grid[x+1][y] if x < N-1 else -1)
    X.append(grid[x-1][y] if x > 0   else -1)
    X.append(grid[x][y+1] if y < N-1 else -1)
    X.append(grid[x][y-1] if y > 0   else -1)

    if grid[x][y] == 0:
        return False
    elif grid[x][y] == 1:
        return True
    elif grid[x][y] == 2:
        return 1 in X
    elif grid[x][y] == 3:
        return 1 in X and 2 in X
    elif grid[x][y] == 4:
        return (1 in X) and (2 in X) and (3 in X)
    else:
        return 1 in X and 2 in X and 3 in X and 4 in X


def sumgrid(grid):
    sum = 0
    for row in grid:
        for y in row:
            sum += y
    return sum

def printgrid(grid):
    print "============="
    print sumgrid(grid)
    for row in grid:
        print row

def getNum(x,y):
    high = 4 if (x == 0 or x == N-1 or y == 0 or y == N-1) else 5  
    return random.randint(1,high)
    
def zerogrid(grid):
    for x in range(N):
        for y in range(N):
            grid[x][y] = 0

def pairs_range(limit):
    for i1 in range(limit):
        for i2 in range(limit):
            yield i1, i2

grid = [[2,3,5],[3,3,3],[5,1,1]]
#grid = [[2,2,1],[2,2,1],[1,2,1]]

#init_list = []
#for x in range(N):
#    for y in range(N):
#        init_list.append(y)

#print init_list
#sys.exit()

grid = []
for x in range(N):
    row = []
    for y in range(N):
        row.append(0)
    
    grid.append(row)



go = False
sum = 0 
while(not go or sum < SUM):
    zerogrid(grid)
    sum = 0
    for x, y in pairs_range(N):
        if not grid[x][y] == 0:
            continue

        r = getNum(x, y)
        grid[x][y] = r
        if r == 5:
            five_neighbors = set([])
            num = 0
            if not grid[x-1][y] == 0:
                five_neighbors.add(grid[x-1][y])
                num += 1
            if not grid[x+1][y] == 0:
                five_neighbors.add(grid[x+1][y])
                num += 1
            if not grid[x][y-1] == 0:
                five_neighbors.add(grid[x][y-1])
                num += 1
            if not grid[x][y+1] == 0:
                five_neighbors.add(grid[x][y+1])
                num += 1
            to_add = FIVE_SET-five_neighbors
            if len(to_add) > (4-num):
                break
            while len(to_add) > 0:
                n = random.sample(to_add, 1)[0]
                to_add.remove(n)
                if grid[x-1][y] == 0:
                    grid[x-1][y] = n
                    continue
                if grid[x+1][y] == 0:
                    grid[x+1][y] = n
                    continue
                if grid[x][y-1] == 0:
                    grid[x][y-1] = n
                    continue
                if grid[x][y+1] == 0:
                    grid[x][y+1] = n
                    continue
                

#        if r == 4:
#            four_neighbors = set([])
#            num = 0
#            if not grid[x-1][y] == 0:
#                four_neighbors.add(grid[x-1][y])
#                num += 1
#            if not grid[x+1][y] == 0:
#                four_neighbors.add(grid[x+1][y])
#                num += 1
#            if not grid[x][y-1] == 0:
#                four_neighbors.add(grid[x][y-1])
#                num += 1
#            if not grid[x][y+1] == 0:
#                four_neighbors.add(grid[x][y+1])
#                num += 1
#            to_add = FOUR_SET-four_neighbors
#            # use 4 because that's the amout that are available
#            if len(to_add) > (4-num):
#                break
                

    
    if sumgrid(grid) >= SUM:
        printgrid(grid)
        go = isGood(grid)

