import sys

defvalue = " "


board = {
    "topL" : defvalue , "topM" : defvalue , "topR" : defvalue ,
    "midL":  defvalue , "midM" : defvalue , "midR" : defvalue,
    "lowL" : defvalue , "lowM" : defvalue , "lowR" : defvalue
    }

quit=[0]

alias = { 1 : "topL" , 2:"topM" , 3:"topR" , 4:"midL" , 5:"midM" , 6:"midR" , 7:"lowL" , 8:"lowM" , 9:"lowR"  }



def printBoard():
    print(     board["topL"] + " |" + board["topM"] + " |" + board["topR"] + "\n" +
            " " + "-+-"   +             "-+-"   +" " +"\n"+

            board["midL"]  + " |" + board["midM"] + " |"  + board["midR"] + "\n" +
             " " + "-+-"   +             "-+-"   +" " +"\n"+
            board["lowL"] + " |" + board["lowM"] + " |" + board["lowR"] + "\n"
    )

printBoard()



def inpt():
    print(" enter the position where you want to insert : " )
    userInput = input()
    return userInput


def inptcheck(turn):
    temp = inpt()
    sucess = "false"

    if board[temp] == defvalue:
        board[temp] = turn
        sucess = "true"
        check(turn)

    if sucess == "false":
        print("that place is already filled")
        inptcheck(turn)
    return



def zerothTurn():
    print("X turn " + "\n" )
    inptcheck("X")
    printBoard()
    return 1



def firstTurn():
    print("O turn " + "\n")
    inptcheck("O")
    printBoard()
    return 0





def check(turn):

    if( (turn==board["topL"] and turn == board["topM"] and turn == board["topR"]) or
        (turn==board["midL"] and turn == board["midM"] and turn == board["midR"]) or
        (turn==board["lowL"] and turn == board["lowM"] and turn == board["lowR"]) or
        (turn==board["topL"] and turn == board["midL"] and turn == board["lowL"]) or
        (turn==board["topM"] and turn == board["midM"] and turn == board["lowM"]) or
        (turn==board["topR"] and turn == board["midR"] and turn == board["lowR"]) or
        (turn==board["topL"] and turn == board["midM"] and turn == board["lowR"]) or
        (turn==board["topR"] and turn == board["midM"] and turn == board["lowL"]) ):

        print( " Player " + turn + " has won the game " )
        quit[0] = 1
    return




def start():
    turn = 0

    while quit[0] == 0:

        if(turn==0):

            turn = zerothTurn()

        else:
            turn  = firstTurn()


start()
