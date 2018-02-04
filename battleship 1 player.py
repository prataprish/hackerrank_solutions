import random
def show(n,board,i,j):
    if board[i][j] == 'h'and (i!=0 or i!=n-1) and (j!=0 or j!=n-1):
        if board[i+1][j] == '-':
            return str(i+1)+" "+str(j)
        elif board[i-1][j] == '-':
            return str(i-1)+" "+str(j)
        elif board[i][j+1] == '-':
            return str(i)+" "+str(j+1)
        elif board[i][j-1] == '-':
            return str(i)+" "+str(j-1)
    elif board[i][j] == 'h' and (i==0 or i==n-1) and (j!=0 or j!=n-1):
        if i == 0:
            if board[i+1][j] == '-':
                return str(i+1)+" "+str(j)
        elif i == n-1:
            if board[i-1][j] == '-':
                return str(i+1)+" "+str(j)
        elif board[i][j+1] == '-':
            return str(i)+" "+str(j+1)
        elif board[i][j-1] == '-':
            return str(i)+" "+str(j-1)
    elif board[i][j] == 'h' and (j==0 or j==n-1) and (i!=0 or i!=n-1):
        if j == 0:
            if board[i][j+1] == '-':
                return str(i)+" "+str(j+1)
        elif j == n-1:
            if board[i][j-1] == '-':
                return str(i)+" "+str(j-1)
        elif board[i+1][j] == '-':
            return str(i+1)+" "+str(j)
        elif board[i-1][j] == '-':
            return str(i-1)+" "+str(j)    
n = int(input())
board = []

hx = 0
ii = 0
jj = 0
for i in range(n):
    board.append(input())
for i in range(1,n-1):
    for j in range(1,n-1):
        if board[i][j] == 'h':
            if (i!=0 or i!=n-1) and (j!=0 or j!=n-1):
                if board[i+1][j]=="-" or board[i-1][j]=="-" or board[i][j+1]=="-" or board[i][j-1]=="-":
                    hx = 1
                    ii = i
                    jj = j
            elif (i!=0 or i!=n-1) and (j==0 or j==n-1):
                if j==0:
                    if board[i+1][j]=="-" or board[i-1][j]=="-" or board[i][j+1]=="-":
                        hx = 1
                        ii = i
                        jj = j
                else:
                    if board[i+1][j]=="-" or board[i-1][j]=="-" or board[i][j-1]=="-":
                        hx = 1
                        ii = i
                        jj = j
            elif (i==0 or i==n-1) and (j!=0 or j!=n-1):
                if i==0:
                    if board[i][j+1]=="-" or board[i][j-1]=="-" or board[i+1][j]=="-":
                        hx = 1
                        ii = i
                        jj = j  
                else:
                    if board[i][j+1]=="-" or board[i][j-1]=="-" or board[i-1][j]=="-":
                        hx = 1
                        ii = i
                        jj = j 
                        
                
for k in range(n):    
    if hx == 1:
        print(show(n,board,ii,jj))
        hx = 0
        break

    else:    
        x = random.randrange(9)
        y = random.randrange(9)
        if board[x][y] == '-':
            print(x,end=" ")
            print(y)
            break
        
        
