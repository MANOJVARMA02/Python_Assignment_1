import getpass
try:
    def main():
        n = input("Do you want to start the game (Y|N):")
        lst=['y','Y','N','n']
        if(n not in lst):
              raise Exception
        while n == "Y" or n == 'y':
            print("Enter your choice from rock,paper,scissor : ")
            player1 = getpass.getpass("Player 1's turn : ")
            player2 = getpass.getpass("Player 2's turn : ")
            player1 = player1.lower()
            player2 = player2.lower()
            if(player1 == player2):
                print("It's a tie!")
            elif((player1=="rock"and player2=="scissor") or (player1=="paper" and player2=="rock")or(player1=="scissor" and player2=="paper")):
                print("Player 1  wins!")
            elif((player1=="scissor"and player2=="rock") or (player1=="rock" and player2=="paper")or(player1=="paper" and player2=="scissor")):
                print("Player 2 wins!")
            else :
                print("Wrong choice")
            n = input("Do you want to play another game(Y|N) :")
            if(n not in lst):
                raise Exception
    main()
except:
    print("Wrong input")