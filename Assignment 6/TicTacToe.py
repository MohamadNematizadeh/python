import pyfiglet
def chek_game():
    for j in range(3):
        if game_board[j][0] == "X" and game_board[j][1] == "X" and game_board[j][2] == "X" or game_board[0][j] == "X" and game_board[1][j] == "X" and game_board[2][j] == "X" or game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X" or game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
            print("player 1 win!")
            b = time.time()
            print(b - a)
            exit()
        if game_board[j][0] == "O" and game_board[j][1] == "O" and game_board[j][2] == "O" or game_board[0][j] == "O" and game_board[1][j] == "O" and game_board[2][j] == "O" or game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O" or game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
            print("player 2 win!")
            b = time.time()
            print(b - a)
            exit()
def player1():
    while True:
        print("Player 1")
        while True:
            row = int(input("row: "))
            col = int(input("col: "))
            if 0 <= row <= 2 and 0<= col <=2:
                if game_board[row][col]=="-":
                    game_board[row][col] = "X"
                    break
                else:
                    print("jer nazan:/")
            else:
                print("mese adam vard kon :!")
        show()
        Chek_game()

    def player_2CU():

     l = 0
    while True:
        if l == 9:
            print("DRAW")
            b = time.time()
            print(b - a)
            exit()

        print("player 1")
        while True:
            satr = int(input("satr: "))
            soton = int(input("soton: "))

            row = int(input("row: "))
            col = int(input("col: "))
            if 0 <= row <= 2 and 0<= col <=2:
                if game_board[row][col]=="-":
                    game_board[row][col] = "X"
                    break
                else:
                    print("jer nazan:/")
            else:
                print("mese adam vard kon :!")
        show()

        if l == 9:
            print("DRAW")
            b = time.time()
            print(b - a)
            exit()

        print("player 2")
        while True:
            satr = random.randint(0,2)
            soton = random.randint(0,2)

            if game_board[satr][soton] == "-":
                l = l + 1
                game_board[satr][soton] = "O"
                break
            
            else:
                print("khone por hast")
                print("dobare emtehan kon")
    
        show()
        chek_game()


def show():
  for row in game_board:

   for cell in row:

        print(cell,end=" ")
print() 
def Chek_game():
    if game_board[0][0] =="X" and game_board[0][1]== "X" and game_board[0][2]=="x":
        print("player 1 wins")
        

title =pyfiglet.figlet_format("Tic Tac Toe",font="slant")

print(title)

game_board = [["-","-","-"],
             ["-","-","-"],
             ["-","-","-"]]

show()



game_mod = input("player_1 or P2: ")

if game_mod == "player_1":
    player1()
if game_mod == "P2":
    player_CU()