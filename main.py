from tkinter import *

root = Tk()
# canvas1
top = Canvas(master=root,height=100,width=50)
top.pack(side= TOP)

#canvas2
left = Canvas(master=root,height=200,width=90)
left.pack(side= LEFT)

#canvas3
right = Canvas(master=root,height= 200,width= 60)
right.pack(side= RIGHT)

#message for number 1 canvas
message = Label(master= top, text="Connect-4:")
message.pack()


board  = [[''] * 7 for i in range(6)]
for i in range(len(board)):
    for j in range(len(board[0])):
        a = Label(master=left, text=board[i][j],relief=SUNKEN,padx=20,pady=20)
        a.grid(row = i, column = j)

player = 0
game_won = False
COLUMN_SIZE = 7
ROW_SIZE = 6

def print_winning_message():
    global game_won 
    if game_won :
        if player == 0:
            l = Label(master=top, text="Connect 4 - **** B WON !!!****",relief=SUNKEN,padx=20,pady=20)
            l.pack()
        else:
            l = Label(master=top, text="Connect 4 - **** A WON !!!!****",relief=SUNKEN,padx=20,pady=20)
            l.pack()


def is_game_won(last_row, last_col):
    global board
    global player
    global game_won
    board = []
    for i in range(6):
        row = []
        for j in range(7):
            f = left.grid_slaves(row=i,column=j)[0]
            row.append(f.cget("text"))
        board.append(row)

    if player == 1:
        return check_if_there_is_a_winner("A", last_row, last_col)
    else:
        return check_if_there_is_a_winner("B", last_row, last_col)

def check_if_there_is_a_winner(player, last_row, last_col):
    global board
    global game_won

    if check_stones_horizontally(board, player, last_row, last_col):
        game_won = True
        return True
    if check_stones_vertically(board, player, last_row, last_col):
        game_won = True
        return True
    if check_stones_up_right_diagonally(board, player, last_row, last_col):
        game_won = True
        return True
    if check_stones_down_right_diagonally(board, player, last_row, last_col):
        game_won = True
        return True
    
    return False

def changeColor(i):
    global game_won
    global player

    if game_won:
        return

    r = 5
    f = left.grid_slaves(row=r,column=i-1)[0]
    while (f.cget("text") == "A" or f.cget("text") == "B") and r > 0: 
        r -= 1
        f = left.grid_slaves(row=r,column=i-1)[0]
    
    if r < 0:
        return
    
    if r == 0 and (f.cget("text") == "A" or f.cget("text") == "B"):
        return

    if player == 0:
        f.configure(bg="red",text="A")
        player = 1
    else:
        f.configure(bg="blue",text="B")
        player = 0
    
    if is_game_won(r, i-1):
        print_winning_message()

for i in range(1,8):
    b = Button(master=right, text = str(i), command=lambda i=i: changeColor(i),padx=20,pady=20)
    b.grid(row=1,column=i)


def check_stones_horizontally(board, last_player, last_row, last_col):
    
    i = 1
    count = 1
    while (last_col - i >= 0 and board[last_row][last_col - i] == last_player):
        i = i + 1
        count = count + 1
    j = 1
    while (last_col + j <= (7 - 1)
           and board[last_row][last_col + j] == last_player):
        j = j + 1
        count = count + 1
    if count >= 4:
        return True
    else:
        return False


def check_stones_down_right_diagonally(board, last_player, last_row, last_col):
    i = 1
    count = 1

    while (last_row - i >= 0 and last_col - i >= 0
           and board[last_row - i][last_col - i] == last_player):
        count += 1
        i = i + 1

    i = 1
    while (last_row + i < 6 and last_col + i < 7
           and board[last_row + i][last_col + i] == last_player):
        count += 1
        i = i + 1

    return count >= 4


def check_stones_vertically(board, last_player, last_row, last_col):
    i = 1
    count = 1

    while (last_row - i >= 0 and board[last_row - i][last_col] == last_player):
        i = i + 1
        count = count + 1
    j = 1
    while (last_row + j <= (ROW_SIZE - 1)and board[last_row + j][last_col] == last_player):
        j = j + 1
        count = count + 1
    if count >= 4:
        return True
    else:
        return False


def check_stones_up_right_diagonally(board, last_player, last_row, last_col):
    i = 1
    count = 1

    while (last_row + i >= 0 and last_col - i >= 0
           and board[last_row + i][last_col - i] == last_player):
        count += 1
        i = i + 1

    i = 1
    while (last_row - i < 6 and last_col + i < 7
           and board[last_row - i][last_col + i] == last_player):
        count += 1
        i = i + 1

    return count >= 4


def print_board(next_player, last_row, last_col):
    
    if next_player == "A":
        check_if_there_is_a_winner('B',last_row, last_col)
    elif next_player == "B":
        check_if_there_is_a_winner('A',last_row, last_col)
        
root.mainloop()