from Tkinter import *
import ttk
import Tix
board = [   [1,2,9,1,0,0],\
            [1,9,2,1,0,0],\
            [1,1,1,0,0,0],\
            [0,0,0,0,0,0],\
            [0,0,1,1,1,0],\
            [0,0,1,9,1,0], ]
board_show = [  [0,0,0,0,0,0],\
                [0,0,0,0,0,0],\
                [0,0,0,0,0,0],\
                [0,0,0,0,0,0],\
                [0,0,0,0,0,0],\
                [0,0,0,0,0,0],]



#const total block x,y

tot_x = len(board[0])#10
tot_y = len(board)
tot_bomb = 3
block_d = 20 #block is a square
#block_w = 20

#draw black block
blk_x = 0
blk_y = 0
BOMB = 9
game_over = False
def gen_board(dim_x,dim_y):
    return [[0 for i in range( dim_x)] for i in range( dim_y)]

def gen_bomb(x,dim_x,dim_y,board):
    import random
    random.seed()
    for i in range(x):
        n = random.randrange(0,dim_x*dim_y)
        _x = n % dim_x
        _y = n / dim_y
        board[_y][_x] = BOMB
def is_bomb(x,y,board):
    if board[y][x] == BOMB:
        return 1
    else:
        return 0
def cnt_bomb(dim_x,dim_y,board):
    for y in range(dim_y):
        for x in range(dim_x):
            if board[y][x] == BOMB:
                continue
            bomb_cnt = 0
            if x - 1 >=0 and y-1 >=0 :
                bomb_cnt = bomb_cnt + is_bomb(x-1,y-1,board)

            if y - 1 >=0 :
                bomb_cnt = bomb_cnt + is_bomb(x,y-1,board)

            if x + 1 <len(board[0]) and y-1 >=0 :
                bomb_cnt = bomb_cnt + is_bomb(x + 1,y - 1,board)

            if x - 1 >=0 :
                bomb_cnt = bomb_cnt + is_bomb(x-1,y,board)

            if x + 1 <len(board) :
                bomb_cnt = bomb_cnt + is_bomb(x+1, y,board)

            if y + 1 <len(board[0]) and x-1 >=0 :
                bomb_cnt = bomb_cnt + is_bomb(x-1,y+1,board)

            if y + 1 <len(board[0]) and board_show[y+1][x]!=1:
                bomb_cnt = bomb_cnt + is_bomb(x,y+1,board)

            if y + 1 <len(board) and x + 1 <len(board[0]) :
                bomb_cnt = bomb_cnt + is_bomb(x+1,y+1,board)
            board[y][x] = bomb_cnt
_board = gen_board(tot_x,tot_y)
gen_bomb (tot_bomb,tot_x,tot_y,_board)
print _board
cnt_bomb(tot_x,tot_y,_board)
for s in _board:
    print s
def check_board(x,y):
    global game_over 
    if game_over == True:
        return
    print "x:"+ str(x) + " y:"+ str(y)
    if board[y][x] == 9:
        print "x:"+ str(x) + " y:"+ str(y) + " Game Over"
        game_over = True
    #    board_show[y][x]=1
        return

    board_show[y][x]=1
    if board[y][x] != 0:
        return

#check lu u ru -> l r -> bl b br
    if x - 1 >=0 and y-1 >=0 and board_show[y-1][x-1]!=1:
        check_board(x-1,y-1)

    if y - 1 >=0 and board_show[y-1][x]!=1:
        check_board(x,y-1)

    if x + 1 <len(board[0]) and y-1 >=0 and board_show[y-1][x+1]!=1:
        check_board(x + 1,y - 1)

    if x - 1 >=0 and board_show[y][x-1]!=1:
        check_board(x-1,y)

    if x + 1 <len(board) and board_show[y][x+1]!=1:
        check_board(x+1, y)

    if y + 1 <len(board[0]) and x-1 >=0 and board_show[y+1][x-1]!=1:
        check_board(x-1,y+1)

    if y + 1 <len(board[0]) and board_show[y+1][x]!=1:
        check_board(x,y+1)

    if y + 1 <len(board) and x + 1 <len(board[0]) and board_show[y+1][x+1]!=1:
        check_board(x+1,y+1)


def draw(event):
    global c
#    print event.x,event.y
#    print event.x/block_d,event.y/block_d
    x = event.x/block_d
    y = event.y/block_d
    global game_over
    #print "is GameOver ?",game_over
    #if game_over == True:
    #    return

    check_board(x,y)
    print "is GameOver ?",game_over
    global lbl 
    if game_over == True:
        lbl.set("game over")
    redraw(c,event.x/block_d,event.y/block_d)
'''
    global blk_x
    global blk_y

    blk_x = blk_x+1
    if blk_x==tot_x:
        blk_x=0
        blk_y = blk_y+1
        if blk_y==tot_y:
            blk_y = 0
'''

def redraw(c,x,y):
    global tot_x,tot_y
    c.delete(ALL)
    for i in range(tot_y):
        for j in range(tot_x):
            #if i == y and j == x:
            #    c.create_rectangle(0+j*block_d,0+i*block_d,block_d+j*block_d,block_d+i*block_d,fill="black")
            #else:
            #    c.create_rectangle(0+j*block_d,0+i*block_d,block_d+j*block_d,block_d+i*block_d,fill="red")
            if board_show[i][j]!=0:
                if board[i][j] != 0 :
                    c.create_rectangle(0+j*block_d,0+i*block_d,block_d+j*block_d,block_d+i*block_d,fill="green")
                    c.create_text((12+j*block_d,12+i*block_d),text=str(board[i][j]))
                elif board[i][j] == 9 :
                    c.create_rectangle(0+j*block_d,0+i*block_d,block_d+j*block_d,block_d+i*block_d,fill="green")
                    c.create_text((12+j*block_d,12+i*block_d),text="B")

                else:
                    c.create_rectangle(0+j*block_d,0+i*block_d,block_d+j*block_d,block_d+i*block_d,fill="green")
            else:
                c.create_rectangle(0+j*block_d,0+i*block_d,block_d+j*block_d,block_d+i*block_d,fill="red")
                if game_over == True and board[i][j] == 9:
                    c.create_text((12+j*block_d,12+i*block_d),text="B")

# main start
root = Tk()
lbl = StringVar()
lbl.set("                   ")
root.title("Board ex")
mainframe = ttk.Frame(root,padding="3 3 12 12") # u b l r

w = ttk.Label(mainframe,text="board ex label",textvariable=lbl)
b = ttk.Button(mainframe,text="click")

# canvas w = block_d * tot_x,h so on...
c = Canvas(mainframe,width=block_d * tot_x,height=block_d * tot_y)

mainframe.grid(column=0,row=0)
w.grid(column=0,row=0,rowspan=2)
b.grid(column=1,row=1)
c.grid(column=0,row=2,columnspan=2)

c.bind("<Button-1>",draw)

#check_board(3,3)

redraw(c,0,0)
root.mainloop()

