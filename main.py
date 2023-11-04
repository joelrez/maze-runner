import csv
import numpy as np 
import math

puzzle = open('puzzle/puzzle1.csv', 'r')

board = []

for row in csv.reader(puzzle):
    board.append(row)

board = np.char.array(board)

num_moves = 0
S = np.where(board.find('S') == 0)
E = np.where(board.find('E') == 0)


class position:
    def __init__(self,y,x,score,move):
        self.pos = (y,x)
        self.y = y
        self.x = x
        self.move = move
        self.score = score
    
    def __eq__(self, o):
        if o == None:
            return False
        elif self.pos == o.pos:
            return True
        else:
            return False
    
    def __str__(self):
        return '<' + str(self.pos) + ', \"' + self.move + '\", ' + str(self.score) + '>'
    
    def __repr__(self):
        return self.__str__()
    
    def __lt__(self, o):
        return self.score < o.score
        
def checkPos(x,y):
    if board[(y,x)] == 'x':
        return False
    else:
        return True

def calcDist(y,x):
    return math.sqrt((y-E[0][0])**2+(x-E[1][0])**2)

def calcF(y,x):
    if checkPos(x,y):
        return num_moves + 1 + calcDist(y,x)
    else:
        return -1

def genPossibleMoves(y,x):
    return [position(y-1, x, calcF(y-1, x), 'up'), position(y+1, x, calcF(y+1,x), 'down'), position(y, x+1, calcF(y, x+1), 'right'), position(y, x-1, calcF(y, x-1), 'left')]

def nextNode(moves):
    cur_pos = moves[len(moves)-1]
    
    possib_moves = genPossibleMoves(cur_pos.y, cur_pos.x)
    for i in range(0,len(possib_moves)):
        pos = min(possib_moves)
        possib_moves.remove(pos)
        if calcDist(pos.y, pos.x) == 0:
            moves.append(pos)
            return moves
        elif pos.score >= 0 and not(pos in moves):
            tmoves = moves.copy()
            tmoves.append(pos)
            moveset = nextNode(tmoves)
            
            if moveset == None:
                next
            else:
                moves.append(pos)
                return nextNode(moves)
            
    return None

def startNode(Sy, Sx):
    # Move selection
    moves = nextNode([position(Sy, Sx, 0, 'start')])
    
    if moves == None:
        print("Solving this puzzle is impossible")
    
    else:
        print('Puzzle Complete! See moves:')
        print(moves)
    
    
Sx = S[1][0]
Sy = S[0][0]

startNode(Sy, Sx)