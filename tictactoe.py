#Tic Tac Toe game in python

board= [" " for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == " " #is gonna give a true or false value

def printBoard(board):
    print("   |   |  " + "     " +"   |   |  ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + "     " + " 1 | 2 | 3 " )
    print("   |   |  " + "     " +"   |   |  ")
    print("-----------" + "     " + "-----------" )
    print("   |   |  " + "     " +"   |   |  ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + "     " + " 4 | 5 | 6 ")
    print("   |   |  " + "     " +"   |   |  ")
    print("-----------" + "     " + "-----------" )
    print("   |   |  " + "     " +"   |   |  ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + "     " + " 7 | 8 | 9 ")
    print("   |   |  " + "     " +"   |   |  ")

def isWinner(bo, le): #bo = board  le= letter
    
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or  (bo[1] == le and bo[2] == le and bo[3] == le) or   (bo[2] == le and bo[5] == le and bo[8] == le) or  (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)


def playerMove():
    run = True
    while run:
        move = input("Please select a position to place an X (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter("X", move)
                else: 
                    print("This space is not FREE, choose another space")
            else:
                print("place type a number with in the range")
        except:
            print("Please type a number")


def compMove(): # 5 steps for de IA
    possibleMoves = [x for x, letter in enumerate(board) if letter== " " and x !=0] #an anumerate gives any index and values of the board
    move = 0

    for let in ["O", "X"]: #first gona chek if O can win and letter if X can win
        for i in possibleMoves: #this try evry empty space for a wining move if is win we retun that wining move
            boardCopy = board[:] #to make a copy we put a : inside
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]: #chekc if the corners are free and add in the list
            cornersOpen.append(i)
        
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]: #check if the corners are free and add in the list
            edgesOpen.append(i)
        
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move



def selectRandom(li):
    import random
    ln = len(li) #gona be the lenght of the list
    r = random.randrange(0,ln)
    return li[r]


def isBoardFull(board):
    if board.count("  ") > 1: 
        return True
    else:
        return False

def main():
    print("Wellcome to the game of Tic Tac Toe!  ")
    printBoard(board)

    while not (isBoardFull(board)):
        if not(isWinner(board, "O")): #this is to check if the PC has won
            playerMove()
            printBoard(board)
        else:
            print("SORRY MATE the pc won.")
            input("THE END")
            break


        if not(isWinner(board, "X")): #this is to check if the PLAYER has won
            move = compMove()
            if move == 0: #the computer cud get a move
                print("TIE GAME!")
                input("THE END")
            else: 
                insertLetter("O", move)
                print("Computer placed and O in postion", move, ":")

                printBoard(board)

        else:
            print("You WON vs an IA!!Good Job")
            input("THE END")
            break

    if isBoardFull(board):
        print("TIE GAME!")
        input("THE END")

main()