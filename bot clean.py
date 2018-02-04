#!/usr/bin/python

# Head ends here
def next_move(posr, posc, board):
    k = 0
    d = []
    shor_ = 0
    shortest = 0
    b = complex(posc,posr)
    for i in board:
        for j in range(len(i)):
            if i[j]=='d':
                d.append(complex(j,k))
        k = k + 1
    for i in range(len(d)):
        if i == 0:
            shortest = abs(b-d[i])
            shor_ = i
        elif shortest > abs(b-d[i]):
            shortest = abs(b-d[i])
            shor_ = i
    mx = posc 
    my = posr
    
    x = int(mx - d[shor_].real)
    y = int(my - d[shor_].imag)
    
    if x == 0 and y == 0:
        print("CLEAN")
        
        
    if x < 0:
        x = -1*x
        print("RIGHT")
    elif x > 0:
        print("LEFT") 
    elif y < 0:
        y = -1*y
        print("DOWN")
    elif y > 0:
        print("UP")
    
        
      
# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
