board = [   [1,2,9,1,0,0],\
            [1,9,2,1,0,0],\
            [1,1,1,1,0,0],\
            [0,0,0,0,0,0],\
            [0,0,1,1,1,0],\
            [0,0,1,9,1,0], ]

board_show = [  [0,0,0,0,0,0],\
                [0,0,0,0,0,0],\
                [0,0,0,0,0,0],\
                [0,0,0,0,0,0],\
                [0,0,0,0,0,0],\
                [0,0,0,0,0,0],]



def check_board(y,x):
    print "x:"+ str(x) + " y:"+ str(y)
    board_show[y][x]=1
    if board[y][x] != 0:
        return

#check lu u ru -> l r -> bl b br
    if x - 1 >=0 and y-1 >=0 and board_show[y-1][x-1]!=1:
        check_board(y-1,x-1)

    if y - 1 >=0 and board_show[y-1][x]!=1:
        check_board(y-1,x)

    if x + 1 <len(board[0]) and y-1 >=0 and board_show[y-1][x+1]!=1:
        check_board(y - 1,x + 1)

    if x - 1 >=0 and board_show[y][x-1]!=1:
        check_board(y,x-1)

    if x + 1 <len(board) and board_show[y][x+1]!=1:
        check_board(y, x+1)

    if y + 1 <len(board[0]) and x-1 >=0 and board_show[y+1][x-1]!=1:
        check_board(y+1,x-1)

    if y + 1 <len(board[0]) and board_show[y+1][x]!=1:
        check_board(y+1,x)

    if y + 1 <len(board) and x + 1 <len(board[0]) and board_show[y+1][x+1]!=1:
        check_board(y+1,x+1)


check_board(3,3)
for i in range(len(board)):
    s = ""
    for j in range(len(board[0])):
        s = s + " "+ str(board_show[i][j])
    print s

