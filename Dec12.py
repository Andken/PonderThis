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
TWO_SET = set([1])
ONE_SET = set([])

WORKING_SET = [set([]), ONE_SET, TWO_SET, THREE_SET, FOUR_SET, FIVE_SET]

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

    high = 5
    if (x == 0 or x == N-1 or y == 0 or y == N-1):
        high = 4
        if (x == 0 or x == N-1) and (y == 0 or y == N-1):
            high = 3

    return random.randint(1,high)
    
def zerogrid(grid):
    for x in range(N):
        for y in range(N):
            grid[x][y] = 0

def pairs_range(limit):
    for i1 in range(limit):
        for i2 in range(limit):
            yield i1, i2

def insert(grid, n, x, y):
    neighbors = set([])
    directions = ['L', 'R', 'U', 'D']
    if x > 0:
        if not grid[x-1][y] == 0:
            neighbors.add(grid[x-1][y])
            directions.remove('L')
    else:
        directions.remove('L')
    if x < N-1:
        if not grid[x+1][y] == 0:
            neighbors.add(grid[x+1][y])
            directions.remove('R')
    else:
        directions.remove('R')
    if y > 0:
        if not grid[x][y-1] == 0:
            neighbors.add(grid[x][y-1])
            directions.remove('U')
    else:
        directions.remove('U')
    if y < N-1:
        if not grid[x][y+1] == 0:
            neighbors.add(grid[x][y+1])
            directions.remove('D')
    else:
        directions.remove('D')

    to_add = WORKING_SET[n]-neighbors

    if len(to_add) > len(directions):
        return False
    grid[x][y] = n
    while len(to_add) > 0:
        n = random.sample(to_add, 1)[0]
        to_add.remove(n)

        pos = random.sample(directions, 1)[0]
        directions.remove(pos)

        if pos == 'L':
            grid[x-1][y] = n
        elif pos == 'R':
            grid[x+1][y] = n
        elif pos == 'U':
            grid[x][y-1] = n
        else:
            grid[x][y+1] = n
    
    return True


grid = [[2,3,5],[3,3,3],[5,1,1]]
#grid = [[2,2,1],[2,2,1],[1,2,1]]

grid = []
for x in range(N):
    row = []
    for y in range(N):
        row.append(0)
    
    grid.append(row)


#### test code
#while(True):
#    print "========\n== NEW ==\n========="
#    zerogrid(grid)
#    printgrid(grid)
#    grid[0][1] = 3
#    grid[1][0] = 1
#    grid[1][2] = 0
#    grid[2][1] = 0
#    print insert(grid, 3, 1, 1)
#    printgrid(grid)

#sys.exit()
#### test code




go = False
sum = 0 
while(not go):
    zerogrid(grid)
    sum = 0
    for x, y in pairs_range(N):
        if not grid[x][y] == 0:
            continue

        r = getNum(x, y)
        if not insert(grid, r, x, y):
            break
    
    if sumgrid(grid) >= SUM:
        printgrid(grid)
        go = isGood(grid)

printgrid(grid)
