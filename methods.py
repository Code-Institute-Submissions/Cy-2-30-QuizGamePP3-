from colorama import Fore

#def validate_name(player):

def print_scoreboard(records):
    """
    Display statistics
    """

    #new_player = [len(records) + 1, player_name, score, f"{int(score / question_num * 100)}%", f"{timer_end:.2f}"]
    #ScoreBoard.append_row(new_player) #add records on google sheets

    view_scoreboard = input(Fore.GREEN + "\nDo you want to view the scoreboard for all played games? (yes/no): " + Fore.RESET).lower()

    if view_scoreboard == "yes":
        # Fetch and display records from Google Sheets
        print(Fore.YELLOW + "\n Players' Scorebord:")
        
        for i,  record in enumerate(records, start= 1):
            if i == 1:
                print(f"{record[0]} | {record[1]} | {record[2]} | {record[3]} | {record[4]}")
            else:
                print(f"{i-1} | {record[1]} | {record[2]} | {record[3]} | {record[4]}")

        #all_players = Player.fetch_all_players(ScoreBoard)
        #display_scoreboard(all_players)

def print_end_game_results(player_name, score, question_num, timer_end):
    """
    Prints the game statisctic at the end
    """
    print("Game Over!")
    print(f"\n{player_name}, here is your score: {score}/{question_num}")
    print(f"Score percentage: {int(score / question_num * 100)}%")
    print(f"Time it took to complete: {timer_end:.2f} seconds")


def print_game_rules():
    """
    Game instructions and rules
    """
    print(Fore.RED +"Game Rules!")
    print(Fore.CYAN +"******************************" + Fore.GREEN )
    print("\nThere are 20 questions in total to complete the game.")
    print("\nThere are 3 guesses allocated, to complete all questions.")
    print("\nIf all guesses are finished, ")
    print("\nafter each wrong answer the game will pass to the next question.")  
    print("\nThere is a timer when completing the questions.")
    print("\nThe score percentage would be given at the end with ratings compared")
    print("\nto other players.")  
    print(Fore.CYAN +"******************************\n")
    time.sleep(3)
    print(Fore.MAGENTA + "Extra Notes!")
    print(Fore.CYAN +"******************************" + Fore.MAGENTA)
    print("\nThere are random facts about the game, ")
    print("\nWhich some of them give hints to some questions in the game.")
    print("\nKeep your eyes open for those hints!") 
    print(Fore.CYAN +"******************************\n")
    time.sleep(5)
    






def checkNum():
    """
    Checks for numbers in the name
    """



def checkCharc():
    """
    Checks for number of charectors in the name
    """




def questions():
    """
    It pulls questions and displays in
    """




def guess():
    """
    Checks number of guesses
    """




def clear():
    """
    Clears the terminal
    """
    os.system('clear' if os.name == 'posix' else 'cls') 



