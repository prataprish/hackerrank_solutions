#!/usr/bin/python
from random import shuffle
# Head ends here
def mapingDirties(posr, posc,board,dim1,dim2):
    dirties=list()
    dirties.append([posr,posc])
    for i in range(0,dim1):
        for j in range(0,dim2):
            if(board[i][j]=='d'):
                dirties.append([i,j])
    mat=[[abs(dirties[x][0]-dirties[y+1][0])+abs(dirties[x][1]-dirties[y+1][1]) for x in range(y+1)] for y in range(len(dirties)-1)]
    return mat,dirties
def search(path,costs):
    loop=0
    improvement = True
    n=len(path)
    while improvement and loop<n*n:
        improvement = False
        for i in range(1, n-1):
            for j in range(i+1, n):
                loop=loop+1
                if(j==n-1):
                    actualPathCost = getCostBetweenCities(costs,path[i-1], path[i]) 
                    newPathCost = getCostBetweenCities(costs,path[i-1], path[j]) 
                else:
                    
                    actualPathCost = getCostBetweenCities(costs,path[i-1], path[i]) + getCostBetweenCities(costs,path[j], path[j+1]) 
                    newPathCost = getCostBetweenCities(costs,path[i-1], path[j]) + getCostBetweenCities(costs,path[i], path[j+1])
                if actualPathCost>newPathCost:
                    temp = path[i]
                    path[i] = path[j]
                    path[j] = temp
                    improvement = True           
    return path
def getCostBetweenCities(costs, point1, point2):
    if point1 < point2:
        return costs[point2-2][point1-1]
    else:
        return costs[point1-2][point2-1]

def getTotalCost(costs, path):
    cost = 0
    for i in range(0, len(path)-1):
        j = i+1
        cost += getCostBetweenCities(costs,path[i], path[j])
    return cost
def next_step(oldposr,oldposc,newposr,newposc):
    aux1=oldposr-newposr
    aux2=oldposc-newposc
    if(aux1!=0):
        if(aux1<0):
            print("DOWN")
        else:
            print("UP")
    else:
        if(aux2<0):
            print("RIGHT")
        else:
            print("LEFT")
def test_move(posr, posc, board,dim1,dim2):
    mat,dirties=mapingDirties(posr, posc,board,dim1,dim2)
    path=[y+1 for y in range(1,len(dirties))]
    solutions=list()
    for i in range(0,dim1*dim2*4):
        solutions.append(path)
        shuffle(solutions[i])
        solutions[i]=[1]+solutions[i]
        solutions[i]=search(solutions[i],mat)
    bestsolution=solutions[0]
    bestcost=getTotalCost(mat, solutions[0])
    for i in range(1,dim1*dim2*4):
        custo=getTotalCost(mat, solutions[i])
        if(custo<bestcost):
            bestsolution=solutions[0]
            bestcost=custo
    
    return bestcost
def next_move(posr, posc,dim1,dim2, board):
    if(board[posr][posc]=='d'):
        print("CLEAN")
        board[posr][posc]='b'
        return
    else:
        bestcost=9999
        i=posr
        j=posc
        if(posr-1>=0):
            cost=test_move(posr-1,posc,board,dim1,dim2)

            if(cost<bestcost):
                bestcost=cost
                move=1
                i=posr-1
                j=posc
                
        if(posr+1<dim1):
            cost=test_move(posr+1,posc,board,dim1,dim2)

            if(cost<bestcost):
                bestcost=cost
                i=posr+1
                j=posc
                
        if(posc-1>=0):
            cost=test_move(posr,posc-1,board,dim1,dim2)

            if(cost<bestcost):
                bestcost=cost
                j=posc-1
                i=posr
             
        if(posc+1<dim2):
            cost=test_move(posr,posc+1,board,dim1,dim2)

            if(cost<bestcost):
                bestcost=cost
                j=posc+1
                i=posr
                
        next_step(posr,posc,i,j)
        board[posr][posc]='-'
        if(board[i][j]!='d'):
            board[i][j]='b'
            

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
