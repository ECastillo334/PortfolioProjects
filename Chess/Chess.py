import pygame
import time
import sys

class Node: #Each square on the board is a Node
    def __init__(self, row, column, width):
        self.row = row
        self.col = column
        self.x = int(row * width)
        self.y = int(column * width)
        if (int(row) + int(column))/2 == (int(row) + int(column))//2:
            self.color = BLACK
        else:
            self.color = WHITE
        self.occ = None
        self.OGcolor = self.color
        pass

    def draw(self, Window):
        pygame.draw.rect(Window, self.color, (self.x, self.y, 100, 100))
        pass

    def setup(self, Window):
        if startingOrder[(self.row, self.col)]:
            if startingOrder[(self.row, self.col)] != None:
                Window.blit(startingOrder[(self.row, self.col)],(self.x, self.y))
        pass

class Piece: #Each Piece follows this class
    def __init__(self, color, name, image):
        self.color = color
        self.name = name
        self.image = image
        self.killable = False
        if name == 'king' or name == 'rook':
            self.castlable = True
        else:
            self.castlable = False
        self.enpassantable = False
        self.see = []
        pass
    
def updateSee(board): #Using this to try to update piece.see. This works with no problems.
    for x in range(0, 8):
        for y in range(0, 8):
            if type(board[x][y]) == Piece:
                board[x][y].see = movetype(board[x][y], [x, y])
                #print(board[x][y].name, '=', board[x][y].see)
                deselect()
    pass


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(j, i, gap)
            grid[i].append(node)
            if (i+j)%2 ==1:
                grid[i][j].color = WHITE
    return grid
    pass

def draw_grid(Window, rows, width):
    gap = width // 8
    for i in range(rows):
        pygame.draw.line(Window, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(Window, GREY, (j * gap, 0), (j * gap, width))
    pass

def update_display(win, grid, rows, width): #This is needed to update the display
    for row in grid:
        for box in row:
            box.draw(win)
            box.setup(win)
    draw_grid(win, rows, width)
    pygame.display.update()
    pass

def findNode(pos):
    y, x = pos
    row = y//100
    column = x//100
    return int(row), int(column)
    pass

def onBoard(pos):
    if pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7:
        return True
    else:
        return False
    pass

def Wpawnmove(currentposition):
    if currentposition[0] == 6:
        if board[currentposition[0]-1][currentposition[1]] == ' ':  
            if board[currentposition[0]-2][currentposition[1]] == ' ':
                board[currentposition[0]-2][currentposition[1]] = "x"
            board[currentposition[0]-1][currentposition[1]] = "x"
    check3 = []
    for i in range(-1, 2):
        check3.append((currentposition[0] - 1, currentposition[1] + i))
    for pos in check3:
        if onBoard(pos): 
            if check3.index(pos)//2 == check3.index(pos)/2:
                try:
                    if board[pos[0]][pos[1]].color != WHITE and pos[0] != (currentposition[0]+1):
                        board[pos[0]][pos[1]].killable = True
                except:
                    pass
            else:
                if board[pos[0]][pos[1]] == ' ':
                    board[pos[0]][pos[1]] = 'x'
    try:
        if board[currentposition[0]][currentposition[1]-1].enpassantable == True and board[currentposition[0]-1][currentposition[1]-1] == ' ':
            board[currentposition[0]-1][currentposition[1]-1] = 'x'
            #print("enpassant to the left")
    except:
        #print("White exception 1")
        None
    try:
        if board[currentposition[0]][currentposition[1]+1].enpassantable == True and board[currentposition[0]-1][currentposition[1]+1] == ' ':
            board[currentposition[0]-1][currentposition[1]+1] = 'x'
            #print("enpassant")
    except:
        #print("White exception 2")
        None
    return board
    pass

def Bpawnmove(currentposition):
    if currentposition[0] == 1:
        if board[currentposition[0]+1][currentposition[1]] == ' ':
            if board[currentposition[0]+2][currentposition[1]] == ' ':
                board[currentposition[0]+2][currentposition[1]] = "x"
            board[currentposition[0]+1][currentposition[1]] = "x"
    check3 = []
    for i in range(-1, 2):
        check3.append((currentposition[0] + 1, currentposition[1] + i))
    for pos in check3:
        if onBoard(pos): 
            if check3.index(pos)//2 == check3.index(pos)/2:
                try:
                    if board[pos[0]][pos[1]].color != BLACK:
                        board[pos[0]][pos[1]].killable = True
                except:
                    pass
            else:
                if board[pos[0]][pos[1]] == ' ':
                    board[pos[0]][pos[1]] = 'x'
    try:
        if board[currentposition[0]][currentposition[1]-1].enpassantable == True and board[currentposition[0]+1][currentposition[1]-1] == ' ':
            board[currentposition[0]+1][currentposition[1]-1] = 'x'
            #print("enpassant")
    except:
        #print("Black exception 1")
        None
    try:
        if board[currentposition[0]][currentposition[1]+1].enpassantable == True and board[currentposition[0]+1][currentposition[1]+1] == ' ':
            board[currentposition[0]+1][currentposition[1]+1] = 'x'
            #print("enpassant")
    except:
        #print('Black exception 2')
        None
    return board
    pass

def PawnPromotion(currentposition, board): #Function that does the pawn promotion from pawn to queen for both white and black pawns.
    if currentposition[0] == 0:
        board[currentposition[0]][currentposition[1]] = Piece(WHITE, "queen", "WQ.png")
        tup = currentposition[1], currentposition[0]
        startingOrder[tup] = pygame.image.load(Wqueen.image)
        update_display(Window, grid, 8, 8)
    if currentposition[0] == 7:
        board[currentposition[0]][currentposition[1]] = Piece(BLACK, "queen", "BQ.png")
        tup = currentposition[1], currentposition[0]
        startingOrder[tup] = pygame.image.load(Bqueen.image)
        update_display(Window, grid, 8, 8)

def BPassantRemove(board):
    for i in range(0, 8):
        try:
            board[3][i].enpassantable = False
            #print(board[3][i].enpassantable)
        except:
            None
    pass

def WPassantRemove(board):
    for i in range(0, 8):
        try:
            board[4][i].enpassantable = False
            #print(board[4][i].enpassantable)
        except:
            None
    pass

def Rookmove(currentpos): #Run through each line in cross and if it finds a piece thats a king and if it finds it return that direction in a list, if not clear list and find a new direction. New functions maybe?
    cross = [[[currentpos[0] + i, currentpos[1]] for i in range(1, 8 - currentpos[0])], [[currentpos[0] - i, currentpos[1]] for i in range(1, currentpos[0] + 1)], [[currentpos[0], currentpos[1] + i] for i in range(1, 8 - currentpos[1])], [[currentpos[0], currentpos[1] - i] for i in range(1, currentpos[1] + 1)]]
    for line in cross:
        Continue = True
        for pos in line:
            if Continue == True:
                if onBoard(pos):
                    if board[pos[0]][pos[1]] == ' ':
                        board[pos[0]][pos[1]] = 'x'
                    elif board[pos[0]][pos[1]].color != board[currentpos[0]][currentpos[1]].color:
                        board[pos[0]][pos[1]].killable = True
                        Continue = False
                        #print('Continue now equals false')
                    elif board[pos[0]][pos[1]].color == board[currentpos[0]][currentpos[1]].color:
                        Continue = False
    return board
    pass

def CheckRook(currentpos): #Possible solution (Probably) (Hopefully)
    cross = [[[currentpos[0] + i, currentpos[1]] for i in range(1, 8 - currentpos[0])], [[currentpos[0] - i, currentpos[1]] for i in range(1, currentpos[0] + 1)], [[currentpos[0], currentpos[1] + i] for i in range(1, 8 - currentpos[1])], [[currentpos[0], currentpos[1] - i] for i in range(1, currentpos[1] + 1)]]
    for line in cross:
        Rlst = []
        for pos in line:
            try:
                if board[pos[0]][pos[1]].name == 'king':
                    return Rlst
            except:
                Rlst.append(pos)
    return None
    pass


def Knightmove(currentpos):
    """for i in range(-2, 3):
        for j in range(-2, 3):
            if i"""
    moves = [[currentpos[0]+2, currentpos[1]+1], [currentpos[0]-2, currentpos[1]+1], [currentpos[0]+2, currentpos[1]-1], [currentpos[0]-2, currentpos[1]-1], [currentpos[0]+1, currentpos[1]+2], [currentpos[0]+1, currentpos[1]-2], [currentpos[0]-1, currentpos[1]+2], [currentpos[0]-1, currentpos[1]-2]]
    for pos in moves:
        if onBoard(pos):
            if board[pos[0]][pos[1]] == ' ':
                    board[pos[0]][pos[1]] = 'x'
            elif board[pos[0]][pos[1]].color != board[currentpos[0]][currentpos[1]].color:
                board[pos[0]][pos[1]].killable = True
    return board
    pass

def Bishopmove(currentpos):
    diagonals = [[[currentpos[0] + i, currentpos[1] + i] for i in range(1, 8)], [[currentpos[0] + i, currentpos[1] - i] for i in range(1, 8)], [[currentpos[0] - i, currentpos[1] + i] for i in range(1, 8)], [[currentpos[0] - i, currentpos[1] - i] for i in range(1, 8)]]
    for direction in diagonals:
        Continue = True
        for pos in direction:
            if Continue == True:
                if onBoard(pos):
                    if board[pos[0]][pos[1]] == ' ':
                        board[pos[0]][pos[1]] = 'x'
                    elif board[pos[0]][pos[1]].color != board[currentpos[0]][currentpos[1]].color:
                        board[pos[0]][pos[1]].killable = True
                        Continue = False
                    elif board[pos[0]][pos[1]].color == board[currentpos[0]][currentpos[1]].color:
                        Continue = False
    return board
    pass

def CheckBishop(currentpos):
    diagonals = [[[currentpos[0] + i, currentpos[1] + i] for i in range(1, 8)], [[currentpos[0] + i, currentpos[1] - i] for i in range(1, 8)], [[currentpos[0] - i, currentpos[1] + i] for i in range(1, 8)], [[currentpos[0] - i, currentpos[1] - i] for i in range(1, 8)]]
    for direction in diagonals:
        Rlst = []
        for pos in direction:
            try:
                if board[pos[0]][pos[1]].name == 'king':
                    return Rlst
            except:
                Rlst.append(pos)
    return None
    pass

def Queenmove(currentpos):
    board = Rookmove(currentpos)
    board = Bishopmove(currentpos)
    return board

def CheckQueen(currentpos):
    Rlst = CheckRook(currentpos)
    if Rlst == None:
        Rlst = CheckBishop(currentpos)
    return Rlst
    pass

def Kingmove(currentpos):
    for x in range(0,3):
        for y in range(0, 3):
            if onBoard((currentpos[0] - 1 + y, currentpos[1] - 1 + x)):
                if board[currentpos[0] - 1 + y][currentpos[1] - 1 + x] == ' ':
                    board[currentpos[0] - 1 + y][currentpos[1] - 1 + x] = 'x'
                else:
                    if board[currentpos[0] - 1 + y][currentpos[1] - 1 + x].color != board[currentpos[0]][currentpos[1]].color:
                        board[currentpos[0] - 1 + y][currentpos[1] - 1 + x].killable = True
#####Castling:########
    if board[currentpos[0]][currentpos[1]].castlable == True:
        Passed = True
        try:
            if board[currentpos[0]][currentpos[1]+3].castlable == True:
                #print('rook has not moved')
                #board[currentpos[0]][currentpos[1]+2] = 'x'
##################^Makes the castle possible#############################
                for i in range(1, 3):
                    if type(board[currentpos[0]][currentpos[1]+i]) == Piece:
                        Passed = False
                if Passed == True:
                    board[currentpos[0]][currentpos[1]+2] = 'x'
                    #print('right castle')
        except:
            None
        try:
            Passed = True
            if board[currentpos[0]][currentpos[1]-4].castlable == True:
                #print('rook has not moved')
                for i in range(1, 4):
                    if type(board[currentpos[0]][currentpos[1]-i]) == Piece:
                        Passed = False
                if Passed == True:
                    board[currentpos[0]][currentpos[1]-2] = 'x'
                    #print('left castle')
        except:
            None
    return board
    pass


def highlight(board):
    Rlst = []
    for i in range(len(board)):
        for x in range(len(board[0])):
            if board[i][x] == 'x':
                Rlst.append([i, x])
            else:
                try:
                    if board[i][x].killable == True:
                        Rlst.append([i, x])
                except:
                    None
    return Rlst
    pass

def undohighlight(grid):
    for i in range(len(grid)):
        for x in range(len(grid[0])):
            grid[i][x].color = grid[i][x].OGcolor
    return grid
    pass

def deselect():
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 'x':
                board[row][column] = ' '
            else:
                try:
                    board[row][column].killable = False
                except:
                    None
            
    pass

def Move(OGPosition, FinalPosition, Window):
    startingOrder[FinalPosition] = startingOrder[OGPosition]
    startingOrder[OGPosition] = None
    pass

def checkforcheck(board, possible, color): 
    for position in possible:
        row = position[0]
        column = position[1]
        try:
            if board[row][column].killable == True and board[row][column].name == "king" and color != board[row][column].color:
                #print('Check!')
                deselect()
                return True
        except:
            None
    deselect()
    return False
    #update_display(Window, grid, 8, 8)
    pass

def movetype(piece, currentpos):
    if piece.name == 'pawn':
        if piece.color == BLACK:
            return highlight(Bpawnmove(currentpos))
        else:
            return highlight(Wpawnmove(currentpos))
    elif piece.name == 'rook':
        return highlight(Rookmove(currentpos))
    elif piece.name == 'knight':
        return highlight(Knightmove(currentpos))
    elif piece.name == 'bishop':
        return highlight(Bishopmove(currentpos))
    elif piece.name == 'queen':
        return highlight(Queenmove(currentpos))
    elif piece.name == 'king':
        return highlight(Kingmove(currentpos))
    pass

#To do's: Stopping discovered check on yourself, castling must check enemy piece.see, king shouldn't be able to move into an attack (Problem area)

#Discovered Check: add to main to check for enemy piece.see

def main(Window): #This is where the magic happens.
    move = 0
    selected = False
    pieceToMove = []
    checked = False
    while True:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if move != 0:
                    if move%2 == 0:
                        WPassantRemove(board)
                    else:
                        BPassantRemove(board)
                #print("event was found")
                mousepos = pygame.mouse.get_pos()
                y, x = findNode(mousepos)
                if selected == False:
                    #print("selected equals false")
                    #print(x, "&", y)
                    #print(movetype(board[x][y], [x]))
                    try:
                        if checked == False or board[x][y].name == 'king': 
                            #print(checked)
                            if move%2 == 0:
                                #print(move)
                                if board[x][y].color == WHITE:
                                    possible = movetype((board[x][y]), [x, y])
                                    for positions in possible:
                                        row = positions[0]
                                        column = positions[1]
                                        grid[row][column].color = BLUE
                                    pieceToMove = x, y
                                    selected = True
                            elif board[x][y].color == BLACK:
                                possible = movetype((board[x][y]), [x, y])
                                for positions in possible:
                                    row = positions[0]
                                    column = positions[1]
                                    grid[row][column].color = BLUE
                                pieceToMove = x, y
                                selected = True
                        else:
                            possible = movetype(board[x][y], [x, y])
                            #print(possible)
                ##############This part handles the attacker coordinates:###################
                            if attacker in possible:
                                #print('attacker is in possible')
                                selected = True
                                grid[attacker[0]][attacker[1]].color = BLUE
                                board[attacker[0]][attacker[1]].killable = True
                                #print(board[attacker[0]][attacker[1]].name, board[attacker[0]][attacker[1]].killable)
                                pieceToMove = x, y
        ##########################This part handles the blocking of check with another piece##################################
                            if blocklst != None and blocklst != [] and possible != None:
                                for pos in possible:
                                    if pos in blocklst:
                                        #print('Found a space to block')
                                        grid[pos[0]][pos[1]].color = BLUE
                                        pieceToMove = x, y
                                        selected = True
                                    else:
                                        try:
                                            if attacker[0] == pos[0] and attacker[1] == pos[1]:
                                                None
                                            else:
                                                board[pos[0]][pos[1]].killable = False
                                        except:        
                                            board[pos[0]][pos[1]] = ' '
                    except:
                        #print("No selected's except happened")
                        pieceToMove = []
                        selected = False
                else:
                    #print("selected is true")
                    #print(pieceToMove)
                    try:
                        if board[x][y].killable == True:
                            row, column = pieceToMove
                            board[x][y] = board[row][column]
                            board[row][column] = ' '
                            deselect()
                            undohighlight(grid)
                            move += 1
                            #print("Just MOve")
                            Move((column, row), (y, x), Window) 
                            if board[x][y].name == 'king' or board[x][y].name == 'rook':
                                board[x][y].castlable = False
                            elif board[x][y].name == 'pawn':
                                PawnPromotion((x, y), board)
                            updateSee(board)
                            checked = checkforcheck(board, movetype((board[x][y]), [x, y]), board[x][y].color)
                            if checked == True:
                                attacker = [x, y]
                                if board[x][y].name == 'rook':
                                    blocklst = CheckRook([x, y])
                                elif board[x][y].name == 'bishop':
                                    blocklst = CheckBishop([x, y])
                                elif board[x][y].name == 'queen':
                                    blocklst = CheckQueen([x, y])
                                else:
                                    blocklst = None
                                #print(blocklst)
                        else:
                            #print("I picked an impossible move")
                            deselect()
                            undohighlight(grid)
                            selected = False
                    except:
                        #print("Other except played")
                        if board[x][y] == 'x':
                            row, column = pieceToMove
                            if board[row][column].name == 'king' and board[row][column].castlable == True: #If the king tries to castle this moves the rook:
                                if y == (column+2):
                                    board[row][(column+1)] = board[row][7]
                                    board[row][7] = ' '
                                    Move((7, row), ((column + 1), x), Window)
                                elif y == (column-2):
                                    board[row][(column-1)] = board[row][0]
                                    board[row][0] = ' '
                                    Move((0, row), ((column-1), x), Window)
                            if board[row][column].name == 'pawn':
                                if (row + 2) == x or (row - 2) == x:
                                    board[row][column].enpassantable = True
                                    #print("This makes a pawn able to be en passanted")
                                elif (column + 1) == y:
                                    #print('en passant capture pleaseeeeee')
                                    board[row][y] = ' '
                                    startingOrder[(y,row)] = None
                                elif (column - 1) == y:
                                    #print('en passant capture pleaseeeeee')
                                    board[row][y] = ' '
                                    startingOrder[(y,row)] = None

                            board[x][y] = board[row][column]
                            board[row][column] = ' '
                            deselect()
                            undohighlight(grid)
                            move += 1
                            Move((column, row), (y, x), Window)
                            if board[x][y].name == 'king' or board[x][y].name == 'rook':
                                board[x][y].castlable = False
                            elif board[x][y].name == 'pawn':
                                PawnPromotion((x, y), board)
                            updateSee(board)
                            checked = checkforcheck(board, movetype((board[x][y]), [x, y]), board[x][y].color)
                            if checked == True:
                                attacker = [x, y] 
                                if board[x][y].name == 'rook':
                                    blocklst = CheckRook([x, y])
                                elif board[x][y].name == 'bishop':
                                    blocklst = CheckBishop([x, y])
                                elif board[x][y].name == 'queen':
                                    blocklst = CheckQueen([x, y])
                                else:
                                    blocklst = None
                        else:
                            #print("I picked a square I can't go to")
                            deselect()
                            undohighlight(grid)
                            selected = False
                    #checkforcheck(board, movetype((board[x][y]), [x, y]), board[x][y].color)
                    selected = False
                #print('Update display should run')
                update_display(Window, grid, 8, 8)
    pass

#Start of initial setup
Window = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Chess")
#COLORS:
WHITE = (105, 113, 131)
GREY = (128, 128, 128)
YELLOW = (204, 204, 0)
BLUE = (50, 255, 255)
BLACK = (41, 57, 39)

#Black Pieces
Brook = Piece(BLACK, "rook", "BR.png")
Bknight = Piece(BLACK, "knight", "BN.png")
Bbishop = Piece(BLACK, 'bishop', "BB.png")
Bqueen = Piece(BLACK, "queen", "BQ.png")
Bking = Piece(BLACK, 'king', "BK.png")
Bpawn = Piece(BLACK, 'pawn', "BP.png")

#White Pieces
Wrook = Piece(WHITE, "rook", "WR.png")
Wknight = Piece(WHITE, "knight", "WN.png")
Wbishop = Piece(WHITE, 'bishop', "WB.png")
Wqueen = Piece(WHITE, "queen", "WQ.png")
Wking = Piece(WHITE, 'king', "WK.png")
Wpawn = Piece(WHITE, "pawn", "WP.png")

#board = [[Brook, Bknight, Bbishop, Bqueen, Bking, Bbishop, Bknight, Brook], [Bpawn, Bpawn, Bpawn, Bpawn, Bpawn, Bpawn, Bpawn, Bpawn], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [Wpawn, Wpawn, Wpawn, Wpawn, Wpawn, Wpawn, Wpawn, Wpawn], [Wrook, Wknight, Wbishop, Wqueen, Wking, Wbishop, Wknight, Wrook]]
board = [[Piece(BLACK, "rook", "BR.png"), Piece(BLACK, "knight", "BN.png"), Piece(BLACK, 'bishop', "BB.png"), Piece(BLACK, "queen", "BQ.png"), Bking, Piece(BLACK, 'bishop', "BB.png"), Piece(BLACK, "knight", "BN.png"), Piece(BLACK, "rook", "BR.png")], 
         [Piece(BLACK, 'pawn', "BP.png"), Piece(BLACK, 'pawn', "BP.png"), Piece(BLACK, 'pawn', "BP.png"), Piece(BLACK, 'pawn', "BP.png"), Piece(BLACK, 'pawn', "BP.png"), Piece(BLACK, 'pawn', "BP.png"), Piece(BLACK, 'pawn', "BP.png"), Piece(BLACK, 'pawn', "BP.png")], 
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
         [Piece(WHITE, "pawn", "WP.png"), Piece(WHITE, "pawn", "WP.png"), Piece(WHITE, "pawn", "WP.png"), Piece(WHITE, "pawn", "WP.png"), Piece(WHITE, "pawn", "WP.png"), Piece(WHITE, "pawn", "WP.png"), Piece(WHITE, "pawn", "WP.png"), Piece(WHITE, "pawn", "WP.png")], 
         [Piece(WHITE, "rook", "WR.png"), Piece(WHITE, "knight", "WN.png"), Piece(WHITE, 'bishop', "WB.png"), Piece(WHITE, "queen", "WQ.png"), Wking, Piece(WHITE, 'bishop', "WB.png"), Piece(WHITE, "knight", "WN.png"), Piece(WHITE, "rook", "WR.png")]]

startingOrder = {(0, 0): pygame.image.load(Brook.image), (1, 0): pygame.image.load(Bknight.image), (2, 0): pygame.image.load(Bbishop.image), (3, 0): pygame.image.load(Bqueen.image), (4, 0): pygame.image.load(Bking.image), (5, 0): pygame.image.load(Bbishop.image), (6, 0): pygame.image.load(Bknight.image), (7, 0): pygame.image.load(Brook.image),(0, 1): pygame.image.load(Bpawn.image), (1, 1): pygame.image.load(Bpawn.image), (2, 1): pygame.image.load(Bpawn.image), (3, 1): pygame.image.load(Bpawn.image), (4, 1): pygame.image.load(Bpawn.image), (5, 1): pygame.image.load(Bpawn.image), (6, 1): pygame.image.load(Bpawn.image), (7, 1): pygame.image.load(Bpawn.image), (0, 2): None, (1, 2): None, (2, 2): None, (3, 2): None, (4, 2): None, (5, 2): None, (6, 2): None, (7, 2): None, (0, 3): None, (1, 3): None, (2, 3): None, (3, 3): None, (4, 3): None, (5, 3): None, (6, 3): None, (7, 3): None, (0, 4): None, (1, 4): None, (2, 4): None, (3, 4): None, (4, 4): None, (5, 4): None, (6, 4): None, (7, 4): None, (0, 5): None, (1, 5): None, (2, 5): None, (3, 5): None, (4, 5): None, (5, 5): None, (6, 5): None, (7, 5): None, (0, 6): pygame.image.load(Wpawn.image), (1, 6): pygame.image.load(Wpawn.image), (2, 6): pygame.image.load(Wpawn.image), (3, 6): pygame.image.load(Wpawn.image), (4, 6): pygame.image.load(Wpawn.image), (5, 6): pygame.image.load(Wpawn.image), (6, 6): pygame.image.load(Wpawn.image), (7, 6): pygame.image.load(Wpawn.image), (0, 7): pygame.image.load(Wrook.image), (1, 7): pygame.image.load(Wknight.image), (2, 7): pygame.image.load(Wbishop.image), (3, 7): pygame.image.load(Wqueen.image), (4, 7): pygame.image.load(Wking.image), (5, 7): pygame.image.load(Wbishop.image), (6, 7): pygame.image.load(Wknight.image), (7, 7): pygame.image.load(Wrook.image)}

draw_grid(Window, 8, 800)
grid = make_grid(8, 800)
update_display(Window, grid, 8, 8)
#End of initial setup

main(Window)