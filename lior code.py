import random


##insert two names into list
def pName():
    player1 = input("Player 1 please enter your name:")
    player2 = input("Player 2 please enter your name:")
    players = [player1, player2]
    return players


##random first player
def radPlayer(players):
    cp = random.choice(players)
    return cp


##player's choice:
def choose_w(players):
    x = True
    while x == True:
        opt = ["💧", "🔥", "☣", "🍄"]
        print(f'You can choose from follow:\n 1-{opt[0]}\t2-{opt[1]}\t3-{opt[2]}\t4-{opt[3]}')
        p1chose = int(input(f'{players[0]} Your choice:')) - 1
        p2chose = int(input(f'{players[1]} Your choice:')) - 1
        if p1chose != p2chose:
            sure = input("are you sure? y/n")
            if sure.lower() == "y":
                p1chose = opt[p1chose]
                p2chose = opt[p2chose]
                playerchoice = {players[0]: p1chose, players[1]: p2chose}
                x = False
            else:
                x = True
        else:
            print("CANT BE THE SAME")

    return playerchoice


##change players
def crUser(cp, players):
    if cp == players[0]:
        return players[1]
    else:
        return players[0]


#print board
def create_board():
    tables = [[["", "", ""], ["", "", ""], ["", "", ""]],
              [["", "", ""], ["", "", ""], ["", "", ""]],
              [["", "", ""], ["", "", ""], ["", "", ""]]]
    return tables


##board
def print_board(tables):
    for z in range(3):
        print(f'===Table {z + 1}===')
        print()
        for x in range(3):
            print("\n+---+---+---+")
            print("|", end="")
            for y in range(3):
                print(" ", tables[x][y][z], end=" |")
        print("\n+---+---+---+")


##place new move
def move(tables, playerchoice, cp):
    print(f'Now it is {cp} turn ')
    x = False
    while x == False:
        try:
            newmovet = int(input("Choose Board:(1,2,3)")) - 1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")
            continue
        newmover = int(input("Now Choose Row:(1-3 up to down)")) - 1
        newmovec = int(input("Now Choose Column:(1-3 left to right)")) - 1
        if tables[newmovet][newmover][newmovec] != "":
            print("Already taken, try again")
            x = False
        else:
            tables[newmovet][newmover][newmovec] = playerchoice[cp]
            print_board(tables)
            x = True

    return tables

##check win
def is_Win(boards, playerchoice, cp):
    # Check for horizontal wins on each table
    for i in range(3):
        for j in range(3):
            if all(boards[i][j][k] == playerchoice[cp] for k in range(3)):
                return True

    # Check for vertical wins on each table
    for i in range(3):
        for k in range(3):
            if all(boards[i][j][k] == playerchoice[cp] for j in range(3)):
                return True

    # Check for diagonal wins on each table
    if all(boards[i][i][i] == playerchoice[cp] for i in range(3)):
        return True

    if all(boards[i][i][2-i] == playerchoice[cp] for i in range(3)):
        return True

    if all(boards[i][j][i] == playerchoice[cp] for i in range(3) for j in range(3)):
        return True

    if all(boards[i][2-j][i] == playerchoice[cp] for i in range(3) for j in range(3)):
        return True

    if all(boards[i][j][j] == playerchoice[cp] for i in range(3) for j in range(3)):
        return True

    if all(boards[i][j][2-j] == playerchoice[cp] for i in range(3) for j in range(3)):
        return True

    # If none of the above conditions are true, the player hasn't won
    return False


def win_Display():
    print("""
            dP   dP   dP dP 888888ba  888888ba   88888888b  888888ba  
            88   88   88 88 88    `8b 88    `8b  88         88    `8b 
            88  .8P  .8P 88 88     88 88     88 a88aaaa    a88aaaa8P' 
            88  d8'  d8' 88 88     88 88     88  88         88   `8b. 
            88.d8P8.d8P  88 88     88 88     88  88         88     88 
            8888' Y88'   dP dP     dP dP     dP  88888888P  dP     dP 
            oooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
            """)

##winners board -how to do file?
def winners_B(cp, winnerdic):
    if cp not in winnerdic:
        winnerdic[cp] = 1
    else:
        winnerdic[cp] += 1
    return winnerdic
def main():
    ans = "y"
    while ans.lower() == "y":
        players = pName()
        ans = input(f'Players names are: \n===> {players[0]} and {players[1]} <===\n do you want to change name? \n(hint:press y/n)')
        if ans.lower() == "n":
            print("GOOD LUCK")
        cp = radPlayer(players)
        print(f'First player to play is:\n=== {cp} ===')
        playerchoice = choose_w(players)
        boards = create_board()
        print_board(boards)
        winnerdic = {}
        while not is_Win(boards, playerchoice, cp):
            boards = move(boards, playerchoice, cp)
            if is_Win(boards, playerchoice, cp):
                win_Display()
                winnerdic = winners_B(cp, winnerdic)
                break
            cp = crUser(cp, players)
            print_board(boards)
        print("== WINNER | WINS ===")
        for key, value in winnerdic.items():
            print(f'{key} | {value}', end=" ")
            print()

main()