# Note: The numpad is supposed to be the index representation of the board
# A 


# from IPython.display import clear_output <-- Clears previous output, only works in Jupyter

def display_board(board):
    print(board[7], " | ", board[8]," | ", board[9])
    print("_____________")
    print(board[4], " | ", board[5]," | ", board[6])
    print("_____________")
    print(board[1], " | ", board[2]," | ", board[3])
    




board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(board)



def player_input(int_player_start):
    
    player2_shape = ""
    
    while True:
        
        player1_shape = input("Player 1 input a shape 'X' or 'O' to choose your shape: ")
        print("")
        
        if player1_shape != "X" and player1_shape != "O":
            print("Please input a valid shape, with capitalized letter")
            continue
        
        elif player1_shape == "X":
            player2_shape = "O"
            break
        else:
            player2_shape = "X"
            break
    
    # klargör vem som börjar av de två spelarna och ser över om deras int input är korrekt med brädan
    # (denna behövs egentligen inte, det var jag som missuppfattade uppgiften)
    while True:
        if int_player_start == 1:
            position = input(f"{player1_shape} : Player 1 starts, enter a valid number 1-9 to start playing: ")
        else:
            position = input(f"{player2_shape} : Player 2 starts, enter a valid number 1-9 to start playing: ")
        if position.isdigit() and int(position) in range(1,10):
            position = int(position)
            print("")
            return position, player1_shape, player2_shape
        else:
            continue
            


def place_marker(board, marker, position):
    #ta in brädans lista och ändra markörer på den motsvarande spelarens markör
    
    board[position] = marker
    return board




def win_check(board, mark):
    
    if board[1] == board[2] == board[3] == mark:
        print("Player", mark, "has won!")
        return True
    elif board[4] == board[5] == board[6] == mark:
        print("Player", mark, "has won!")
        return True
    elif board[7] == board[8] == board[9] == mark:
        print("Player", mark, "has won!")
        return True
        
    counter = 0
    # En alternativ lösning:
    # Följer mönster för rader, nedersta raden adderas med ett, därefter adderas +3 på countern, detta motsvarar vertikala rader
    for x in board:
        counter += 1
        if counter == 4:
            break
        if board[counter] == board[counter+3] == board[counter+3+3] == mark:
            print(f"Player with shape {board[counter]} has won!")
            return True
    
    # Wincheck for diagonal
    if board[1] == board[5] == board[9] == mark:
        print("Player", board[1], "has won!")
        return True
        
        
    elif board[3] == board[5] == board[7] == mark:
        print("Player", board[3], "has won!")
        return True
        


import random

def choose_first():
    int_random_player_start = random.randint(1, 2)
    return int_random_player_start
    


# Checks if there's space on the board
def space_check(board, position):
    # Kollar om en index i listan är populerad med X eller O
    if board[position] == "X" or board[position] == "O":
        return False
    else:
        return True
    

# The game can sometimes tie and the result of this is when the board is full
# This counter will count each X and O in the list and when the count reaches 9 the game is a tie
def full_board_check(board):
    full_counter = 0
    
    for x in board:
        
        if x == "X" or x == "O":
            full_counter += 1
            
            if full_counter == 9:
                print("Board is full, the game is a tie!")
                return True
            
    #return full_counter 




def player_choice(board, player, shape):
    # kanske behöver passera in space_check funktionen här eller när jag kör alltihop
    while True:
        number_input = input(f"{shape} : {player} pick your next placement between 1-9: ")
        
        if number_input.isdigit() and int(number_input) in range(1,10):
            number_input = int(number_input)
            if space_check(board, number_input) == True: # kör space check funktionen med positionen och ser om det är ledigt
                return number_input
            else:
                print("Pick a placement that is not occupied")
        else:
            print("Pick a valid number in the range 1-9")
            


def replay():
    # Function asks if they want to play again, returns True if yes and returns False if not 
    # If incorrect input please input valid character
    while True:
        play_again = input("Do you want to play again? Y/N?: ")
        if play_again == "Y":
            return True
        elif play_again == "N":
            return False
        else:
            print("Enter 'Y' or 'N' with capital letter to choose if you want to play again")



print('Welcome to Tic Tac Toe!')
print("")

while True:
    # Set the game up here
    game_on = True
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    print("This is the board:")
    print("")
    display_board(board) # Shows the board
    
    # assigns an int, 1 or 2 to the variable
    int_random_player_start = choose_first()
    
    # returns a number to start playing, player1shape and player2shape
    start_position, player1_shape, player2_shape = player_input(int_random_player_start) 
    
    
    # if int is 1, player 1 starts, else its player 2
    if int_random_player_start == 1:
        place_marker(board, player1_shape, start_position)
    else:
        place_marker(board, player2_shape, start_position)
    

    while game_on:
        print("")
        display_board(board) # prints the board after every placement
        int_random_player_start +=1
        
        #Player 1 Turn
        if int_random_player_start%2 == 1:
            position = player_choice(board, "Player 1", player1_shape)
            
            place_marker(board, player1_shape, position)
            game_check = win_check(board, player1_shape)
            
            # Kollar om det är en win eller om brädan är full, detta görs innan loopen kör om igen då game_on måste bli False innan
            if game_check == True or full_board_check(board) == True:
                print("")
                display_board(board)
                game_on = False
        
        
        # Player2's turn.
        if int_random_player_start%2 == 0:
            position = player_choice(board, "Player 2", player2_shape)
            
            place_marker(board, player2_shape, position)
            game_check = win_check(board, player2_shape)
            
            if game_check == True or full_board_check(board) == True:
                print("")
                display_board(board) # Visa brädan efter vinst eller oavgjort
                game_on = False
                
    if not replay():
        break
        # Denna befinner sig i första while loopen, om denna blir false så bryter den ut ur den, om inte så startar första loopen om igen        
        
        
