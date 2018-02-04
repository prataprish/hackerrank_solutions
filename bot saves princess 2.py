#
def nextMove(n,r,c,grid):
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
    
    if x<0:
        return("RIGHT")
    if x>0:
        return("LEFT")
    if y<0:
        return("DOWN")
    if y>0:
        return("UP")

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
