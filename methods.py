from colorama import Fore
import os 
import time
from classes import Player 
from flask import Flask, request, jsonify, render_template
import gspread
from google.oauth2.service_account import Credentials
import sys

SCOPE = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive"
        ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('quizgamepp3') 
ScoreBoard = SHEET.worksheet('gameresults') 
records = ScoreBoard.get_all_values()


def print_game_rules():
    """
    Game instructions and rules
    Game hints 
    """
    time.sleep(2)
    print(Fore.RED + " Game Rules!")
    print(Fore.CYAN + " ******************************" + Fore.GREEN )
    time.sleep(2)
    print("\n There are 20 questions in total to complete the game.")
    print("\n There are 3 guesses allocated, to complete all questions.")
    print("\n If all guesses are finished, ")
    print("\n after each wrong answer the game will pass to the next question.")  
    print("\n There is a timer when completing the questions.")
    print("\n The score percentage would be given at the end with ratings compared")
    print("\n to other players.")  
    print(Fore.CYAN + " \n ******************************\n")

    time.sleep(4)

    next()
    print(Fore.CYAN + " \n ******************************")
    print(Fore.MAGENTA + " Extra Notes!")
    print(Fore.CYAN + " ******************************" + Fore.MAGENTA)
    print("\n There are random facts about the game, ")
    print("\n Which some of them give hints to some questions in the game.")
    print("\n Keep your eyes open for those hints!") 
    print(Fore.CYAN + " \n ******************************\n")


def quiz(ScoreBoard, questions, fun_facts, player_name):
    """
    Quiz questions game start and end when questions reaches 20
    """
    score = 0
    guesses = 3
    question_num = 5
    timer_start = time.time() #start counting from game start

    clear()
    
    for i, question in enumerate(questions, 1):
        if i > question_num:
            break # Stops when questions reaches 20
    
        clear()
        print(Fore.YELLOW + " Did you know!" + Fore.CYAN)
        print(" ******************************" + Fore.GREEN)
        print(f"{fun_facts[i - 1]}")
        print(Fore.CYAN + " ******************************" + Fore.RESET)

        print(f"\nQuestion {i}: {question['question']}\n")
        for j, option in enumerate(question["options"], 1):
            print(f"{j}. {option}")  # Print number and option

        while True:
            player_answer = input(" Input your answer (Please enter 1, 2, or 3) : ")
            
            if player_answer.isdigit() and 1 <= int(player_answer) <= 3:
                if question["options"][int(player_answer) - 1] in question["answer"]:
                    score += 1 # Adds a point for every correct answer 
                    break 

                else:
                    print(" Incorrect! Next question.")
                    break
                
            else:
                print(" Invalid Input! (Please enter 1, 2, or 3) : ")

        time.sleep(1)

    # Calculates the total time taken to complete the game
    timer_end = time.time() - timer_start

    player = Player(player_name, ScoreBoard)
    records = ScoreBoard.get_all_values()
    player.save_player_info(records, score, question_num, timer_end)
    
    print_end_game_results(records, question_num, player_name, score, timer_end)
    time.sleep(5)
    print_scoreboard(records)

    while True:
        end_game = input(Fore.GREEN + "\n Enter 'E' for Exit to end the game. : ")
        # Checks if the player wants to end the game
        if end_game.lower() == "E":
            print(Fore.YELLOW + " Goodbye!")
            time.sleep(4)
            clear()
            print(Fore.GREEN + f"\n Press" + Fore.YELLOW +"'Start Game'" + Fore.GREEN + "button to play again.")
            time.sleep(4)
            sys.exit() 

        else:
            print(" Invalid input!")
            print(end_game)


def print_end_game_results(records, question_num, player_name, score, timer_end):
    """
    Prints the game statisctic at the end
    """
    print(" \nGame Over!")
    print(f"\n {player_name}, here is your score: {score}/{question_num}")
    print(f" Score percentage: {int(score / question_num * 100)}%")
    print(f" Time it took to complete: {timer_end:.2f} seconds")

    
def print_scoreboard(records):
    """
    Display statistics
    """

    #new_player = [len(records) + 1, player_name, score, f"{int(score / question_num * 100)}%", f"{timer_end:.2f}"]
    #ScoreBoard.append_row(new_player) #add records on google sheets

    view_scoreboard = input(Fore.GREEN + "\n Do you want to view the scoreboard for all played games? (yes/no): " + Fore.RESET).lower()

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



def clear():
    """
    Clears the terminal
    """
    os.system('clear' if os.name == 'posix' else 'cls') 

def next():
    """
    Offer an option for player to continue
    """
    while True:
        next = input(Fore.GREEN + f" Enter 'N' for 'Next' to continue: ")
        if next.lower() == "n":
            break

        else:
            print(" Invalid input!")
            print(next) 

        

app = Flask(__name__)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    """
    ERROR ON FORM SUBMISSION AS IT IS NOT SAVING ON TO GOOGLE SHEETS
    On submsion of the form it sends and saves the information 
    into into google sheets
    """
    try:
        #worksheet = SCOPED_CREDS.open('quizgamepp3').feedback NOT NECCESSARY ALREAD DECLARED 

        name = request.form.get('fname')
        last_name = request.form.get('lname')
        email = request.form.get('email')
        message_heading = request.form.get('message')
        message = request.form.get('feedback')

        worksheet.append_row([name,last_name,email,message_heading,message])

        return jsonify({'success': True, 'message':'Form submitted successfully!'})

    except Exception as e:
        return jsonify({'success': False, 'message': f'Error: {str(e)}'})

if __name__ == '__main__':
    app.run(port = 5000)



app.route('/')
def index():
    """
    ERROR!!! IT IS NOT WORKING
    Pulls the data from google sheets to display on on the Scoreboard button window in html file
    """
    data = worksheet

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

