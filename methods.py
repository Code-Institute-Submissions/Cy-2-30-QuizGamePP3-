from colorama import Fore
import os 
import time
from classes import Payer 
from flask import Flask, request, jsonify
import gspread
from google.oauth2.service_account import Credentials

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


#def validate_name(player):

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

def print_end_game_results(player_name, score, question_num, timer_end):
    """
    Prints the game statisctic at the end
    """
    print(" Game Over!")
    print(f"\n {player_name}, here is your score: {score}/{question_num}")
    print(f" Score percentage: {int(score / question_num * 100)}%")
    print(f" Time it took to complete: {timer_end:.2f} seconds")


def print_game_rules():
    """
    Game instructions and rules
    """
    print(Fore.RED + " Game Rules!")
    print(Fore.CYAN + " ******************************" + Fore.GREEN )
    print("\n There are 20 questions in total to complete the game.")
    print("\n There are 3 guesses allocated, to complete all questions.")
    print("\n If all guesses are finished, ")
    print("\n after each wrong answer the game will pass to the next question.")  
    print("\n There is a timer when completing the questions.")
    print("\n The score percentage would be given at the end with ratings compared")
    print("\n to other players.")  
    print(Fore.CYAN + " ******************************\n")

    time.sleep(2)

    print(Fore.MAGENTA + " Extra Notes!")
    print(Fore.CYAN + " ******************************" + Fore.MAGENTA)
    print("\n There are random facts about the game, ")
    print("\n Which some of them give hints to some questions in the game.")
    print("\n Keep your eyes open for those hints!") 
    print(Fore.CYAN + " ******************************\n")

    time.sleep(2)
    






def quiz():
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

app = Flask(__name__)

@app.route('/submit_form', methods=['POST'])

def submit_form():
    """
    ERROR ON FORM SUBMISSION AS IT IS NOT SAVING ON TO GOOGLE SHEETS
    On submsion of the form it sends and saves the information 
    into into google sheets
    """
    try:
        worksheet = SCOPED_CREDS.open('quizgamepp3').feedback

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