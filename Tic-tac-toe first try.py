
# Note: My first attempt at the game without external help

# Att åstadkomma:
# 2 spelare ska kunna spela från samma dator
# Brädan ska printas ut varje gång en spelare gör en move
# Acceptera input från player och placera en symbol på brädan
# Använd "numpad" till att matcha nummer till griden på numpaden

# fråga spelare 1 om de vill vara X eller O

# tre i rad så ska ena spelaren vinna

# Efter vinnare, fråga om de vill fortsätta spela


game_board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "] # La till en tom sträng för att index ska stämma överens med numpad

def board_print():
    print(game_board[7]+"|"+game_board[8]+"|"+game_board[9])
    print("-----")
    print(game_board[4]+"|"+game_board[5]+"|"+game_board[6])
    print("-----")
    print(game_board[1]+"|"+game_board[2]+"|"+game_board[3])
    



def user_input(turn_switch, player1_shape, player2_shape):
    result = "not correct"
    num_check = False
    player = ""
    if turn_switch%2 == 1:
        player = "Spelare 1 : "
        player += player1_shape
    else:
        player = "Spelare 2 : "
        player += player2_shape
    
    # While loopen, tar emot input och verifierar att den stämmer
    while result.isdigit() == False or num_check == False:
        result = input(f"{player}, välj en siffra på din numpad, 1-9: ")
        

        
        # Vi måste ha denna .isdigit() före om result blir angiven en sträng, då blir det error om man int konverterar en sträng. Därför måste man kolla om det är en siffra först.
        if result.isdigit() == True:
            if int(result) in range(1,10):
                if game_board[int(result)] != "X" and game_board[int(result)] != "O":
                    num_check = True
                else:
                    
                    print("En form är redan lagd på denna plats, välj en annan.")
            else:
                print("Vänligen ange en siffra mellan 1-9")
        else:
            print("Vänligen ange en numerisk siffra")
        
    
    return int(result)


# Få inputten från user_input att påverka planen
# Måste ta in vilken spelare som har vilken form, men också vilken spelares tur det är.
# Turordning i samband med form som ska läggas ut måste kopplas ihop 
def applicera_user_input(index_input, player_turn):
    # variabeln player_turn tar in rätt turordning och motsvarande form.
    
    
    game_board[index_input] = player_turn
    
    #clear_output()
    return game_board
    

# Definiera spelare 1 och 2, för att ange input X eller O
# Kommer skapa upp 2 variabler, spelare 1 och spelare 2
# Varje får välja en form som blir kopplad till deras variabel "spelare"
# Det betyder att variabel player_1 kommer innehålla en form
# Tror ett dictionary kan vara en rimlig användning eftersom, player_1 kan vara nyckeln och skriver ut värdet (formen)

def choose_shape():
    player1 = ""
    player2 = ""
    #clear_output()
    # Spelare 1 väljer en form
    while player1 != "X" and player1 != "O":
        player1 = input("Spelare 1 vänligen välj en form, 'X' eller 'O': ")
    
    # Spelare 2 får överbliven form
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
            
    return (player1, player2)




# Skapa upp en spelarordning som använder variablerna från choose_shape
# Denna funktion ska även tillbringa med korrekt turordning för spelare
# Denna funktion ska användas till applicera input funktionen

def player_turn(turn_switch, player1_shape, player2_shape):
    # Ta in de två variablerna från f.d funktionen choose_shape
    # variablerna som tas in har värdena "X" och "O", ordningen kan vara olika.
    
    
    if turn_switch%2 == 1:
        return player1_shape
        
    else:
        return player2_shape
        


def win_check():
    row_bottom = "".join(game_board[1:4])
    row_mid = "".join(game_board[4:7])
    row_top = "".join(game_board[7:10])
    
    column_left = "".join(game_board[1:8:3])
    column_mid = "".join(game_board[2:9:3])
    column_right = "".join(game_board[3:10:3])
    
    diagonal_right = "".join(game_board[1:10:4])
    diagonal_right = "".join(game_board[3:8:2])
    
    
    if game_board[1] == game_board[2] == game_board[3] == "X":
        return True
    elif game_board[4] == game_board[5] == game_board[6] == "X":
        return True
    elif game_board[7] == game_board[8] == game_board[9] == "X":
        return True
    elif game_board[1] == game_board[4] == game_board[7] == "X":
        return True
    elif game_board[2] == game_board[5] == game_board[8] == "X":
        return True
    elif game_board[3] == game_board[6] == game_board[9] == "X":
        return True
    elif game_board[1] == game_board[5] == game_board[9] == "X":
        return True
    elif game_board[3] == game_board[5] == game_board[7] == "X":
        return True
    else:
        pass
    
    if game_board[1] == game_board[2] == game_board[3] == "O":
        return True
    elif game_board[4] == game_board[5] == game_board[6] == "O":
        return True
    elif game_board[7] == game_board[8] == game_board[9] == "O":
        return True
    elif game_board[1] == game_board[4] == game_board[7] == "O":
        return True
    elif game_board[2] == game_board[5] == game_board[8] == "O":
        return True
    elif game_board[3] == game_board[6] == game_board[9] == "O":
        return True
    elif game_board[1] == game_board[5] == game_board[9] == "O":
        return True
    elif game_board[3] == game_board[5] == game_board[7] == "O":
        return True
    else:
        pass
    
    # Oavgjort check
    string_gameboard = "".join(game_board)
    string_gameboard = string_gameboard.replace(" ", "") # Får ut en lista utan mellanslag
    
    if len(string_gameboard) == 9:
        return 2



def play_again_func():
    svar = "input"
    while svar != "J" and svar != "N":
        svar = input("Vill ni köra igen? J/N: ")
        
        if svar == "J":
            play_game()
        else:
            pass




def game_board_reset():
    game_board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    return game_board





def play_game():
    # Logik för alla funktioner
    
    game_on = True
    player1_shape, player2_shape = choose_shape() # Varje spelare får sin form
    
    turn_switch = 0 # Sätter ett statiskt startvärde för växling av spelare (så att det inte återgår till True hela tiden, eftersom att det är en while loop)
    for index in range(1,10):
        game_board[index] = " "
        
    while game_on == True:
        turn_switch+=1
        board_print()
        
        index_input = user_input(turn_switch, player1_shape, player2_shape) # Får ut en integer index som motsvarar placering
        playerturn = player_turn(turn_switch, player1_shape, player2_shape) # Håller koll på turordning och sparar korrekt form i variabel
        applicera_user_input(index_input, playerturn) # Tar in den index plats form ska läggas på, samt korrekt form
        win = win_check()
        if win == True:
            if turn_switch%2 == 1:
                print("Spelare 1 vann!")
                
                board_print()
                
            else:
                print("Spelare 2 vann!")
            break
        elif win == 2:
            print("Det blev oavgjort")
            break
    play_again_func()

play_game()


        
