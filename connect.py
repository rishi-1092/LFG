import sys
X, Y, N = map(int, input().split())
board = [["O"]*Y for _ in range(X)]

for x in range(X):
    row = input().strip().split()
    board[x] = row

def checkForWin ( row, col ):
    winstatus  = False
    global x
    global y
    global N
    dirX = [1 , 0, -1, 0, -1, 1, -1, 1]
    dirY = [0 , 1, 0, -1, -1, 1, 1, -1]
    for i in range(8):
        xdir = dirX[i]
        ydir = dirY[i]
        if (row+((N-1)*xdir) >= 0 ) and (row+((N-1)*xdir) < X ) and (col+((N-1)*ydir) >= 0 ) and (col+((N-1)*ydir) < Y ):
            winstatus = True
            for t in range(N):
                # print(board[row+(t*xdir)][col+(t*ydir)] +"--"+board[row][col])
                # print(str(row+(t*xdir))+","+str(col+(t*ydir)) +"--"+str(row)+","+str(col))
                if board[row+(t*xdir)][col+(t*ydir)] != board[row][col]:
                    # print("row " + str(row+(t*xdir)) + " " + str(row))
                    # print("col " + str(col+(t*ydir)) + " " + str(col))
                    winstatus = False
                    break
            if winstatus == True:
                break
    return winstatus

for x in range(X):
    for y in range(Y):
        if(board[x][y] in  ["B", "R"]):
            if checkForWin(row=x, col=y):
                if board[x][y] == "B":
                    print("BLUE WINS")
                else:
                    print("RED WINS")
                sys.exit(0)
print("NONE")
            
