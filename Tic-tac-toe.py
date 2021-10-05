#Create a list with 9 blank space for a tic tac toe game
blankSpace = [" " for i in range(9)]
#print(blankSpace[0:5]) - checking the output
# Create a tic tac toe in 3X3 pattern
def ticTacToe():
    #using format function for strings to create tic tac toe pattern
    row1 = "|{}|{}|{}|".format(blankSpace[0],blankSpace[1],blankSpace[2])
    row2 = "|{}|{}|{}|".format(blankSpace[3],blankSpace[4],blankSpace[5])
    row3 = "|{}|{}|{}|".format(blankSpace[6],blankSpace[7],blankSpace[8])
    print(row1)
    print(row2)
    print(row3)

def playerMove(icon):
    if icon == "X":
        number = "1"
    elif icon == "O":
        number = "2"
    print("Your turn player {}".format(number))
    choice = int(input("Enter position for {0}: ".format(icon)).strip())
    if (choice < 10):
        if blankSpace[choice - 1] == " ":
            blankSpace[choice - 1] = icon
        else:
            print("That place has been taken!!!")

def isVictory(icon):
    if((blankSpace[0] == icon and blankSpace[1] == icon and blankSpace[2] == icon) or \
       (blankSpace[3] == icon and blankSpace[4] == icon and blankSpace[5] == icon) or \
       (blankSpace[6] == icon and blankSpace[7] == icon and blankSpace[8] == icon) or \
       (blankSpace[0] == icon and blankSpace[3] == icon and blankSpace[6] == icon) or \
       (blankSpace[1] == icon and blankSpace[4] == icon and blankSpace[7] == icon) or \
       (blankSpace[2] == icon and blankSpace[6] == icon and blankSpace[8] == icon) or \
       (blankSpace[0] == icon and blankSpace[4] == icon and blankSpace[8] == icon) or \
       (blankSpace[2] == icon and blankSpace[4] == icon and blankSpace[6] == icon)):
        return True
    else:
        return False

def isDraw():
    if " " not in blankSpace:
        return True
    else:
        return False

while True:
    ticTacToe()
    playerMove("X")
    ticTacToe()
    if isVictory("X"):
        print("Congratulations!!!! You win player 1")
        ticTacToe()
        break
    elif isDraw():
        print("The game is drawn!!!!")
        ticTacToe()
        break
    playerMove("O")
    if isVictory("O"):
        print("Congratulations!!!! You win player 2")
        ticTacToe()
        break
    elif isDraw():
        print("The game is drawn!!!!")
        ticTacToe()
        break
