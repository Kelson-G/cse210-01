# Kelson Gneiting
# Week 1
# Tic-Tac-Toe
# Assignment 1

def main(): 
    game = [1,2,3,4,5,6,7,8,9]
    print("Welcome to Tic Tac Toe. The Board is layed out as shown: \n1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9")
    print("Press a number to begin.")
    length = 3
    while length < 12:
        turn(length,game)
        length += 1
        check(game)
    print("It was a Draw")
    again = input("Want to play again? (Y/N): ")
    if again.upper() == "Y":
        main()
    else:
        quit()

def turn(player,game):
    try:
        if player % 2 == 1:
            symbol = "X"
        else:
            symbol = "O"
        box = int(input("Where would you like your %s: " % (symbol)))
        if box in range(1,10):
            box -= 1
            game.insert(box,symbol)
            box += 1
            game.pop(box)
            print("%s|%s|%s\n-+-+-\n%s|%s|%s\n-+-+-\n%s|%s|%s" % (game[0],game[1],game[2],game[3],game[4],game[5],game[6],game[7],game[8]))
        else:
            print("Invalid Input")
            turn(player,game)
    except ValueError:
        print("Invalid Input")
        turn(player,game)

def check(game):
    winning_sets = {
        1:[1,2,3],
        2:[4,5,6],
        3:[7,8,9],
        4:[1,4,7],
        5:[2,5,8],
        6:[3,6,9],
        7:[1,5,9],
        8:[3,5,7]
    }
    for set in winning_sets:
        if game[winning_sets[set][0]] == game[winning_sets[set][1]] == game[winning_sets[set][2]]:
            print("%s has won!" % (game[winning_sets[set][1]]))
            again = input("Want to play again? (Y/N): ")
            if again.upper() == "Y":
                main()
            else:
                quit()  

if __name__ == "__main__":
    main()