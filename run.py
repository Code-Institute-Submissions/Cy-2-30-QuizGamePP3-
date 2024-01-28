import gspread
from google.oauth2.service_account import Credentials
from colorama import Fore 
import random 
import os
import time
from classes import Player
from methods import (
    print_scoreboard,
    print_end_game_results,
    clear,
    print_game_rules,
    quiz,
    continue_game
)
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

# The quiz questions dictionary
questions = [ 
    {"question" : "Where did the Christmas tree originate from? :", 
    "options"   : ["Germany.", "Ireland.", "Canada."], 
    "answer"    : "Germany."}, 
    {"question" : "What is the highest-grossing Christmas film of all time? :", 
    "options"   : ["Home Alone, raking in $300 million.", "The animated Dr Seuss' The Grinch 2018, raking in $512 million.", "Failure to Launch,raking in $100 million."],
    "answer"    : "The animated Dr Seuss' The Grinch (2018), raking in $512 million."},
    {"question" : "Where do Christmas gonks come from? :", 
    "options"   : ["United States.", "Soviet Union.", "Scandinavia.",],
    "answer"    : "Scandinavia."}, 
    {"question" : "WIn what film would you hear the greeting 'Merry Christmas, ya filthy animal'? :", 
    "options"   : ["Home Alone.", "Chrismas with Family.", "Two Half a Men"], 
    "answer"    : "Home Alone."}, 
    {"question" : "Before turkey, what was the traditional Christmas Day meal in England? :", 
    "options"   : ["The traditional Christmas meal in England was rosted turkey.", "The traditional Christmas meal in England was a pig's head and mustard.", "The traditional Christmas meal in England was roasted ham."], 
    "answer"    : "The traditional Christmas meal in England was a pig's head and mustard."}, 
    {"question" : "Which artist had the most Christmas No.1 singles? :", 
    "options"   : ["The Beatles.", "Westlife.", "Boys to Men."], 
    "answer"    : "The Beatles."}, 
    {"question" : "Who invented electric lights for the Christmas tree? :", 
    "options"   : ["Edward Johnson in the US in 1882.", "John Smith in the UK in 1750.", "Edward Dammes in Germany in 1950."], 
    "answer"    : "Edward Johnson in the US in 1882."}, 
    {"question" : "How much does the world's most expensive Christmas decoration cost? :", 
    "options"   : ["The emu egg set in 24-carat gold cost £8 million.", "The emu egg set in 24-carat gold cost £9 million.", "The emu egg set in 24-carat gold cost £8.9 million."], 
    "answer"    : "The emu egg set in 24-carat gold cost £8.9 million."}, 
    {"question" : "When did John Lewis open its online Christmas shop? :", 
    "options"   : ["31st July 2003.", "31st August 2023.", "31st December 2008."], 
    "answer"    : "31st August 2023."}, 
    {"question" : "Where is the UK's tallest Christmas tree situated? :", 
    "options"   : ["Cape Town", "Kildare", "Wakehurst, West Sussex."], 
    "answer"    : "Wakehurst, West Sussex."},  

    {"question" : "Where is the oldest Christmas market in the world?  :", 
    "options"   :  ["Dresden's Striezelmarkt, Germany.", "Oslo street market, Norway.", "Dublin, chrismas market."], 
    "answer"    : "Dresden's Striezelmarkt, Germany."}, 
    {"question" : "What is a tree with fake snow called? :", 
    "options"   : ["A pine tree.", "A flocked Christmas tree.", "Snowy Christmas tree."], 
    "answer"    : ["A flocked Christmas tree.","Snowy Christmas tree."]}, 
    {"question" : "How many gifts were given in total in 'The Twelve Days of Christmas' song?  :", 
    "options"   : ["365.", "366.", "364."], 
    "answer"    : "364." }, 
    {"question" : "What color are mistletoe berries? :", 
    "options"   : ["White.", "Black.", "Yellow."], 
    "answer"    : "White."}, 
    {"question" : "What is the most popular Christmas plant in the UK? :", 
    "options"   : ["Poinsettia.", "Chrismas lights.", "Mexican flame leaf."], 
    "answer"    : "Poinsettia."}, 
    {"question" : "How tall is the record holder for the tallest-ever snowman? :", 
    "options"   : ["200 feet.", "113 feet.", "213 feet."], 
    "answer"    : "113 feet."}, 
    {"question" : "How many Christmas puddings are sold in the UK on average? :", 
    "options"   : ["2 million.", "250 million.", "25 million."], 
    "answer"    : "25 million."}, 
    {"question" : "Which country donates the Christmas tree in Trafalgar Square? :", 
    "options"   : ["Norway.", "France.", "Germany."], 
    "answer"    : "Norway."},
    {"question" : "Who invented the Christmas cracker? :", 
    "options"   : ["Coonectcut-based confectioner Tom Waffles.", "Munich-based confectioner Gerhard Regards.", "London-based confectioner and baker Tom Smith."], 
    "answer"    : "London-based confectioner and baker Tom Smith."},  
    {"question" : "Where does the name Boxing Day come from? :", 
    "options"   : ["Boxing Day was a traditional day off peace.", "Boxing Day was a traditional day off for servants in which they received a 'Christmas Box' from their master.", "Boxing Day was a traditional day off cleaning and resting after Chrismas Day."], 
    "answer"    : "Boxing Day was a traditional day off for servants in which they received a 'Christmas Box' from their master."},
    
    {"question" : "When was Christmas first celebrated in the UK? :", 
    "options"   : ["In the 20th century.", "In the 6th century.", "In the 1th century."], 
    "answer"    : "In the 6th century."}, 
    {"question" : "How many tips do traditional snowflakes have? :", 
    "options"   : ["Six.", "Seven.", "Nine."], 
    "answer"    : "Six."}, 
    {"question" : "What is the most popular Christmas tree topper ornament? :",
    "options"   : ["The devil.", "The ghost.", "An angel."], 
    "answer"    : "An angel."}, 
    {"question" : "According to UK traditions, when should Christmas decorations come down? :", 
    "options"   : ["Twelfth Night, 5th or 6th January.", "Sixth Night, 15th or 16th January.", "twentyfirst Night, 28th or 29th January."], 
    "answer"    : "Twelfth Night, 5th or 6th January."}, 
    {"question" : "Who started the tradition of exchanging gifts? :", 
    "options"   : ["The French.", "The Romans.", "The Rassians."], 
    "answer"    : "The Romans." }, 
    {"question" : "Where does the tradition of hanging gifts on the Christmas tree come from? :", 
    "options"   : ["The Druids.", "The magicians.", "The Priest."], 
    "answer"    : "The Druids."},
    {"question" : "Why do we give chocolate coins for Christmas? :", 
    "options"   : ["To honor Saint Nicholas.", "To honor St Patrick.", "To honor Chrismas father."], 
    "answer"    : "To honor Saint Nicholas."}, 
    {"question" : "Who wrote A Christmas Carol? :", 
    "options"   : ["Tom Hilfigure.", "Charles Dickens.", "Chulk Bass."], 
    "answer"    : "Charles Dickens."}, 
    {"question" : "What fruit is usually placed in stockings? :", 
    "options"   : ["An apple.", "An apricot.", "An orange."], 
    "answer"    : "An orange."}, 
    {"question" : "What was the Home Alone decor inspired by? :", 
    "options"   : ["Antique paintings.", "Antique cards and Norman Rockwell paintings.", "Chrismas cards."], 
    "answer"    : "Antique cards and Norman Rockwell paintings."},
 
    {"question" : "Who brought the Christmas tree to England? :", 
    "options"   : ["Queen Charlotte, wife of King George III installed the first indoor tree (a yew tree) at Queen's Lodge, Windsor, in 1800 to mark the festive season", "Princess of Denmark, installed the first indoor tree at Queen's Lodge.", "Prince Albert, who, after importing several spruce firs from Germany in 1840, was credited with introducing the Christmas tree tradition to the masses."], 
    "answer"    : ["Queen Charlotte, wife of King George III, installed the first indoor tree (a yew tree) at Queen's Lodge, Windsor, in 1800 to mark the festive season","Prince Albert, who, after importing several spruce firs from Germany in 1840, was credited with introducing the Christmas tree tradition to the masses."]}, 
    {"question" : "Who invented the Christmas wreath? :", 
    "options"   : ["An English Lutheran pastor named Jonh Rich.", "A Rassian Lutheran pastor named Piet Norman.", "A German Lutheran pastor named Johann Hinrich Wichern."], 
    "answer"    : "A German Lutheran pastor named Johann Hinrich Wichern."}, 
    {"question" : "What is the most popular Christmas tree in the UK? :", 
    "options"   : ["Nordmann Smith.", "Nordmann Fir.", "John Norman."], 
    "answer"    : "Nordmann Fir."}, 
    {"question" : "What was the first Christmas tree decoration? :", 
    "options"   : ["Candles, introduced by Martin Luther in Germany.", "Candles, introduced by Martin Luther in USA.", "Candles, introduced by Martin Luther in England."], 
    "answer"    : "Candles, introduced by Martin Luther in Germany."}, 
    {"question" : "When do the 12 days (about 1 week 5 days) of Christmas start? :", 
    "options"   : ["25th December.", "24th December.", "26th December."], 
    "answer"    : "25th December."},
    {"question" : "In which year was the first Christmas card sent? :", 
    "options"   : ["1850.", "1980.", "1843."], 
    "answer"    : "1843."}, 
    {"question" : "Where are the McCallisters going on holiday when they leave Kevin behind in Home Alone? :", 
    "options"   : ["Greese.", "Norway.", "France."], 
    "answer"    : "France."}, 
    {"question" : "Stollen is the traditional fruit cake of which country? :", 
    "options"   : ["Poland.", "Germany.", "France."], 
    "answer"    : "Germany."}, 
    {"question" : "How many real Christmas trees are sold each year in the UK? :", 
    "options"   : ["8 million.", "2 million.", "5 million."], 
    "answer"    : "8 million."},    
    {"question" : "What is the name for the period between Christmas and New Year? :", 
    "options"   : ["Twixmas.", "Year end.", "31 celebration."], 
    "answer"    : "Twixmas."},
  
    {"question" : "What country started the tradition of hanging stockings? :", 
    "options"   : ["Norway.", "Greece.", "Italy."], 
    "answer"    : "Italy."}, 
    {"question" : "How many Christmas trees are grown in Europe each year? :", 
    "options"   : ["60 million.", "200 million.", "66 million."], 
    "answer"    : "60 million."}, 
    {"question" : "What does Holy represent? :", 
    "options"   : ["Jesus Christ's cross.", "Jesus Christ's crown of thorns.", "Jesus Christ's cloth."], 
    "answer"    : "Jesus Christ's crown of thorns."}, 
    {"question" : "When were electric Christmas tree lights invented? :", 
    "options"   : ["1850 by Edward Johnson in the US.", "1881 by Edward Johnson in the US.", "1882 by Edward Johnson in the US."], 
    "answer"    : "1882 by Edward Johnson in the US."},
    {"question" : "Before being developed into a toy, how did Elf on the Shelf begin? :", 
    "options"   : ["Elf on the Shelf began as a children's picture book in 2005.", "Elf on the Shelf began as a children's picture book in 2006.", "Elf on the Shelf began as a children's picture book in 2007."], 
    "answer"    : "Elf on the Shelf began as a children's picture book in 2005."}, 
    {"question" : "Which accessory do you add to the base of your Christmas tree to hide the stand or trunk? :", 
    "options"   : ["Tree skirt.", "Tree star.", "Tree lights."], 
    "answer"    : "Tree skirt."}, 
    {"question" : "When were turkeys first brought to England? :", 
    "options"   : ["1950.", "1880.", "1526."], 
    "answer"    : "1526."}, 
    {"question" : "Aside from a fireplace mantel, where is the most popular place to use a Christmas garland in the home? :", 
    "options"   : ["The stairs.", "Near the window.", "Next to the wood storage."], 
    "answer"    : "The stairs."}, 
    {"question" : "Who designed the upside-down Christmas tree at Claridge's Hotel in 2017? :", 
    "options"   : ["Kelvin Cline.", "Tom Ford.", "Karl Lagerfeld."], 
    "answer"    : "Karl Lagerfeld."},   
    {"question" : "Which country invented glass baubles? :", 
    "options"   : ["Ireland.", "Germany.", "South America."], 
    "answer"    : "Germany."}
    ]

# Fun facts and hints to the quiz game array list
fun_facts = ["Mince pies used to contain real minced beef.", "It is said to be unlucky to eat a mince pie with a knife.", 
            "Christmas pudding used to be a soup.", "Candy canes were invented to keep kids quiet in church.", 
            "Instead of turkey at Christmas, it used to be a pigs head and mustard.","People in Japan eat fast-food chicken on Christmas day.",
            "Father Christmas is called lots of different names all around the world.", "Christmas used to be banned in Scotland.", 
            "In America, they play a game of 'hide the pickle'.", "In Peru, they celebrate Christmas day on Christmas eve.",

            "In Sweden, they leave a coffee for Santa instead of cookies.","The smallest Christmas card ever made is invisible to the human eye.", 
            "Prince Albert introduced the Christmas tree to England in 1800.", "The tinsel on your Christmas tree used to be made from real silver.", 
            "The world record for a Christmas tree is 221 feet.", "Santa Claus makes 842 million stops on Christmas eve night.",
            "London’s Trafalgar Square Christmas tree is a gift from Norway.", "The tree topper tradition began in Victorian times.", 
            "Santa Claus is 1750 years old.", " The only light on Santa’s sleigh is Rudolph’s nose.", 

            "Santa uses nine reindeer to pull his sleigh.", "Santa has 200 000 elves that help him get all the presents ready.",
            "Christmas Wreaths are symbols of Jesus Christ.", "The song 'Jingle Bells' was sent into space.", 
            "Mistletoe is named after the mistle thrush bird.", "Christmas carols are based on the English tradition of wassailing.",
            "Robins are a popular symbol of Christmas because of the postmen.","It took the three kings 12 days to reach the baby Jesus Christ.",
            "Evergreens have been a festive symbol since the time of the Romans and the Ancient Egyptians."," Xmas means the same as Christmas."]

# Chooses questions randomly and facts randomly from the dictionary and array list
random.shuffle(questions) 
random.shuffle(fun_facts)


def main():
    """
    Game introduction
    Player name verification 
    Start Game
    """
   
    # Welcome message 
    print(Fore.GREEN + " Welcome to the Christmas Quiz!")
    print(Fore.CYAN +" ******************************")
    time.sleep(3)

    # Giving the player an option to continue
    continue_game()
    clear()
    print(Fore.YELLOW + " \n Here is the game information!\n")
    print(Fore.CYAN +" ******************************")
    print_game_rules()
    time.sleep(3)
    
    # Giving the player an option to start or exit the game 
    while True:
        start_game = input(Fore.GREEN + "\n Do you want to start the game? (yes/no): ")
        if start_game.lower() == "yes":
            clear()
            player_name = input(" Enter your name(inlude a number and at least 3 letters): ")
            break

        elif start_game.lower() == "no":
            print(Fore.YELLOW + " Goodbye!")
            time.sleep(4)
            clear()
            print(Fore.GREEN + f"\n Press" + Fore.YELLOW +"'Start Game'" + Fore.GREEN + "button to play again.")
            time.sleep(4)
            sys.exit() 

        else:
            print(Fore.RED + "Invalid input! Do you want to start the game? (yes/no): " + Fore.RESET)
    
    # Validate the player name 
    player = Player(player_name, ScoreBoard)
    while not player.validate_name():
        print(Fore.RED + " Invalid name! Please correct: " + Fore.RESET)

        if not player.validate_len():
            print(Fore.YELLOW + " Name must be more than 3 characters." + Fore.RESET)

        elif not player.validate_alnum(): # It is not checking for alphabets or number !!! fix later 
            print(Fore.YELLOW + " Name must have at least one number and alphabet." + Fore.RESET)  
        
        elif player.name_in_scoreboard():
            print(Fore.YELLOW + " Name already exists. Choose a different name." + Fore.RESET)
        
        player_name = input(" Enter your name (inlude a number and at least 3 letters): ")
        player = Player(player_name, ScoreBoard)
    
    # Personalized introduction before game start
    print(Fore.CYAN +" ******************************")
    print(Fore.GREEN + f" {player_name} welcome to... ")
    print(Fore.RED + " Who is in the Festive Spirit?" + Fore.GREEN + " quiz game!")
    print(Fore.CYAN + " ******************************\n")
    time.sleep(3)
    
    # Start game 
    quiz(ScoreBoard, questions, fun_facts, player_name)
    
if __name__ == "__main__":
    main()
