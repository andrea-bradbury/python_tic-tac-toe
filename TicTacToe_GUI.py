'''

Andrea Bradbury
Noughts and Crosses Game - Python Assignment

Task: Develop an OOP analysis of noughts and crosses with a GUI.

This game allows for the user to play the computer. The user is X and always goes first.

The game handles inputs of numbers to choose the user's move on the board.
If an invalid place is selected the user can enter a place again.

The computer's turn is determined by 3 scenarios:
- A place where O will win
- A place where X will win (to defensively guard that spot)
- Otherwise select a corner position
    - The program also contains a safeguard for the computer to chose the first available place on the board.
    (This should never actually be used but is a good back up for piece of mind).

The game handles wins by either user or computer and a draw scenario.

To exit the game the user just needs to click the screen.

'''


import turtle

#Create the turle assets
t= turtle.Turtle()
t.pensize(5)
t.color("bisque")
t.ht()

#For invalid entry pop ups
message = turtle.Turtle()
message.penup()
message.ht()
message.goto(-200, 0)
message.color("medium violet red")

#Screen
screen= turtle.Screen()
screen.tracer(0)
screen.bgcolor("thistle")

#Backend board
Places = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]]


def Game():
    # Method for the main procedure of the game
    drawBoard()
    makeBoardActive()
    screen.exitonclick()

def drawBoard():
    #Creates the lines on the board
    for i in range(2):
        t.penup()
        t.goto(-300, 100-200 * i )
        t.pendown()
        t.forward(600)

    t.right(90)
    for i in range(2):
        t.penup()
        t.goto(-100+200*i, 300)
        t.pendown()
        t.forward(600)
    screen.update()

    #Adds the numbers to the squares for users to choose their spot
    spotNumber = 1
    message.write("Type the corresponding number you'd like to place your move in", font=("Arial", 10))
    for i in range(3):
        for j in range(3):
            t.penup()
            t.goto(-290 + j*200, 260 - i*200)
            t.pendown()
            t.write(spotNumber, font=("Arial", 15))
            spotNumber += 1


def CheckWinner(letter):
    # Check if there's a winner

    #Check row
    for i in range(3):
        if Places[i][0] == Places[i][1] and Places[i][1] == Places[i][2] and Places[i][0] == letter:
            return True
        #Check cols
        if Places[0][i] == Places[1][i] and Places[0][i] == Places[2][i] and Places[0][i] == letter:
            return True

    #Check diag
    if Places[0][0] == Places[1][1] and Places[2][2] == Places[1][1] and Places[0][0] == letter:
        return True

    if Places[0][2] == Places[1][1] and Places[0][2] == Places[2][0] and Places[0][2] == letter:
        return True

    return False

def CheckDraw():
    #Check for number of spare places on the board
    plays = 0
    for i in range(3):
        for j in range(3):
            if Places[i][j] != " ":
                plays += 1
    if plays == 9:
        return True
    else:
        return False

def endGame():
    for i in range(9):
        screen.onkey(None, str(i+1))


def drawX(x,y):
    #Draws an X
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color("dark red")
    t.setheading(60)

    for i in range(2):
        t.forward(75)
        t.backward(150)
        t.forward(75)
        t.left(60)

    screen.update()

def drawO(x, y):
    #Draws a O
    t.penup()
    t.goto(x, y-55)
    t.setheading(0)
    t.color("dark slate blue")
    t.pendown()
    t.circle(50)

    screen.update()


def placeO():
    #Simple AI for computer player

    #Check for a place on the board where O would win
    for i in range(3):
        for j in range(3):
            if Places[i][j] == " ":
                Places[i][j] = "O"
                if CheckWinner("O"):
                    Places[i][j] = "O"
                    drawO(-200 + 200*j, 200-200*i)
                    return
                Places[i][j] = " "
    #Check for a place on the board where X would win
    for i in range(3):
        for j in range(3):
            if Places[i][j] == " ":
                Places[i][j] = "X"
                if CheckWinner("X"):
                    Places[i][j] = "O"
                    drawO(-200 + 200*j, 200-200*i)
                    return
                Places[i][j] = " "
    #If there's no winning or defensive placement available choose a corner
    for i in range(0,3,2):
        for j in range(0,3,2):
            if Places[i][j] == " ":
                Places[i][j] = "O"
                drawO(-200 + 200 * j, 200 - 200 * i)
                return
    #Finding any other empty spot
    for i in range(3):
        for j in range(3):
            if Places[i][j] == " ":
                Places[i][j] = "O"
                drawO(-200 + 200 * j, 200 - 200 * i)
                return


def placeX(row, col ):
    # Check that spot isn't taken
    message.clear()
    if Places[row][col] == "X" or Places[row][col] == "O":
        message.write("You can't take this place, please choose another.", font=("Arial", 15))
        screen.update()
        placeX(makeBoardActive())
    else:
        #Draw the X
        drawX(-200+ 200 * col , 200 -200 * row)

        #Add this place into the back end board Places
        Places[row][col] = "X"
        #message.write("Places "+ str(Places), font=("Arial", 10))

    #Check if won
    if CheckWinner("X"):
        message.goto(-97,0)
        message.write("X Wins!", font=("Arial", 30))
        screen.update()
        endGame()
    else:
    #If no winner, keep asking O for move
        placeO()
        if CheckWinner("O"):
            message.goto(-90, 0)
            message.write("Computer Wins!", font=("Arial", 30))
            screen.update()
            endGame()
            screen.exitonclick()
        #Check Draw
        elif CheckDraw():
            message.goto(-90, 0)
            message.write("It's a draw", font=("Arial", 30))
            screen.update()
            endGame()
            screen.exitonclick()

def square1():
    placeX(0,0)
def square2():
    placeX(0,1)
def square3():
    placeX(0,2)
def square4():
    placeX(1,0)
def square5():
    placeX(1,1)
def square6():
    placeX(1,2)
def square7():
    placeX(2,0)
def square8():
    placeX(2,1)
def square9():
    placeX(2,2)


def makeBoardActive():
    #Makes the user inputs correspond to the square's functions
    screen.listen()
    Events = [square1, square2, square3, square4, square5, square6, square7, square8, square9]

    for i in range(9):
         screen.onkey(Events[i], str(i+1))


Game()
