import random

def  game(your_score, computer_score):
    moves = 'rsp'
    computer_move = random.choice(moves)
    user_move = input("Please state Your move :- ")
    if (user_move == 'r'):
        if(computer_move == 'r'):
            print("\nYour move is ", user_move,".\n"
                  "Computers's move is ", computer_move,".\n"
                  "It's a draw.\n")
            game(your_score, computer_score)
        elif(computer_move == 's'):
            your_score += 1
            computer_score -= 1
            print("\nYour move is ", user_move, ".\n"
                  "Computers's move is ", computer_move, ".\n"
                  "Rock blunts Scissors. YOU WIN !!!\n")
            game(your_score, computer_score)
        elif(computer_move == 'p'):
            your_score -= 1
            computer_score += 1
            print("\nYour move is ", user_move, ".\n"
                  "Computers's move is ", computer_move, ".\n"
                  "Paper Covers Rock. Computer Wins !!\n")
            game(your_score, computer_score)
        game(your_score, computer_score)
    elif (user_move == 's'):
        if(computer_move == 'r'):
            your_score -= 1
            computer_score += 1
            print("\nYour move is ", user_move,".\n"
                  "Computers's move is ", computer_move,".\n"
                  "Rock blunts Scissors. Computer Wins !!\n")
            game(your_score, computer_score)
        elif(computer_move == 's'):
            print("\nYour move is ", user_move, ".\n"
                  "Computers's move is ", computer_move, ".\n"
                  "It's a draw.\n")
            game(your_score, computer_score)
        elif(computer_move == 'p'):
            your_score += 1
            computer_score -= 1
            print("\nYour move is ", user_move, ".\n"
                  "Computers's move is ", computer_move, ".\n"
                  "Scissors cut Paper. YOU WIN !!!\n")
            game(your_score, computer_score)
        game(your_score, computer_score)
    elif (user_move == 'p'):
        if(computer_move == 'r'):
            your_score += 1
            computer_score -= 1
            print("\nYour move is ", user_move,".\n"
                  "Computers's move is ", computer_move,".\n"
                  "Paper covers Rock. YOU WIN !!!\n")
            game(your_score, computer_score)
        elif(computer_move == 's'):
            your_score -= 1
            computer_score += 1
            print("\nYour move is ", user_move, ".\n"
                  "Computers's move is ", computer_move, ".\n"
                  "Scissors cut Paper. Computer Wins !!\n")
            game(your_score, computer_score)
        elif(computer_move == 'p'):
            print("\nYour move is ", user_move, ".\n"
                  "Computers's move is ", computer_move, ".\n"
                  "It's a draw.\n")
            game(your_score, computer_score)
        game(your_score, computer_score)
    elif(user_move == 'e'):
        if(computer_score > your_score):
            print("Final Scores are :-\n Your Score :- ", your_score, "\n Computer's Score :- ", computer_score, "\n\nComputer Wins !!")
        elif(computer_score == your_score):
            print("Final Scores are :-\n Your Score :- ", your_score, "\n Computer's Score :- ", computer_score, "\n\nIt's a Draw !!")
        elif(computer_score < your_score):
            print("Final Scores are :-\n Your Score :- ", your_score, "\n Computer's Score :- ", computer_score, "\n\nYou Win !!!")
        quit()
    else:
        print("Please state a valid move.\n\n")
        game(your_score, computer_score)

print ("Welcome to the Rock, Paper, Scissor game.\n"
       "•Required Abbreviations :-\n"
       "  r for Rock\n"
       "  p for Paper\n"
       "  s for Scissor\n"
       "  e for  Quitting The Game.\n\n"
       "•Rules :-\n"
       "  Rock blunts Scissors\n"
       "  Paper covers Rock\n"
       "  Scissors cut Paper\n\n"
       "•Scoring :-\n"
       "  1 point(s) will be awarded for a win.\n"
       "  -1 point(s) will be awarded for a loss.\n"
       "  0 point(s) will be awarded for a draw.\n\n"
       "You should state your move according to the abbreviations.\n"
       "     (Note :- Please use lowercase letters only.\n"
       "              Final Scores will be shown at the end of the game.)\n\n\n")

game(0,0)
