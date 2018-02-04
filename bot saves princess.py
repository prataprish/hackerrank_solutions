#!/usr/bin/python
def displayPathtoPrincess(n,grid):
    x = 0
    y = 0
    mx=0
    px=0
    my=0
    py = 0
    for i in range(n):
        for j in grid:
            if 'p' == j[i]:
                px = i
            if 'm' == j[i]:
                mx = i
    for i in range(n):
        for j in grid[i]:
            if 'p' in j:
                py = i
            if 'm' in j:
                my = i
    x = mx-px
    y = my-py
    if x < 0:
        x = -1*x
        for i in range(x):
            print("RIGHT")
    else:
        for i in range(x):
            print("LEFT")
    if y < 0:
        y = -1*y
        for i in range(y):
            print("DOWN")
    else:
        for i in range(y):
            print("UP")    
    
#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())
displayPathtoPrincess(m,grid)
