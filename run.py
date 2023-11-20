import gspread
from google.oauth2.service_account import Credentials
#from colorama import Fore
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('quizgamepp3')

teams = SHEET.worksheet('teams')
records = teams.get_all_values()



#game random fun facts
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

#change of game content
"""
# quiz words with 3 levels 1. Easy level 
easy_words =["Elves", "Merry", "Jolly", "Carols", "Myrrh", 
"Xmas", "Birth", "Family", "Candy", "Sleigh",
"Jesus", "Chimney", "Spirit", "Goose", "Angel"
"Tinsel", "Elf", "Feast", "Sledge", "Holly"]

#middle level
middle_words = ["Chrismas","Festive", "Reindeer", "Carolling", "Carolers",
"Frankincense", "Mistletoe", "Nativity", "Tradition", "Fruitcake",
"Rudolph", "Pinecone", "Presents", "Yuletide", "Stocking",
"Tidings", "Holiday	","Chestnuts", "Ornaments", "Snowball"]						

#hard level
hard_words = ["Saint Nicholas", "Santa Claus","Kris Kringle", "Christmas Eve", "Santa\’s helpers",
"North Pole", "Plum pudding", "Gingerbread house", "Frosty the Snowman", "Santa\’s workshop",
"Season\’s greetings", "Christmas card", "Christmas carol", "Christmas tree", "Christmas tree stand",
"December 25", "Jack Frost", "St. Nicks", "Father Christmas", "Sleigh bells"]
"""

random_fact = random.choice(fun_facts)
#random_word = random.choice(easy_words)

print("Did you know!")
print("******************************")
print(random_fact)
print("******************************")

#print("Guess the words...")
#print(random_word)

questions = ("What was the Home Alone decor inspired by? :", 
"What fruit is usually placed in stockings? :", 
"Who wrote A Christmas Carol? :", 
"Why do we give chocolate coins for Christmas? :",
 "Where does the tradition of hanging gifts on the Christmas tree come from? :", 
 "Who started the tradition of exchanging gifts? :")
    
answers  = ("B", "D", "B", "C", "A", "C")

options = (("A. Someone told the movie director.", "B. Antique cards and Norman Rockwell paintings.", "C. The director dreamt about it.", "D. Inspired idea by a child in the movie"),
("A. An apple", "B. Bananas", "C. Grapes", "D. An orange."),
("A. Charles Berry", "B. Charles Dickens.", "C. Donald Trump", "D. Elon Mask"),
("A. Chocolate is good.", "B. Kids love chocolate.", "C. To honour Saint Nicholas.", "D. It is a tradition."),
("A. The Druids.", "B. South America", "C. Slovenia", "D. Rassia"),
("A. African", "B. Brits", "C. The Romans.", "D. Chinese"),)

score = 0
guess = 3
guess_storage = []
question_index = 1
option_index = 0
num_questions = 0

    
for question in questions:
    print(f"\nQestion {question_index}: {question}")
    print("\n******************************")

    for option in options[option_index]: 
        print(option)

    guesses = str(input("Enter your answer (A, B, C, D): ").upper())

    if guesses ==  answers[option_index]:
        score += 1
        print("Next question!")
        print("\n******************************")

    else:
        print("Play again!")

    guesses = str(input("Enter your answer (A, B, C, D): ").upper())
    guess_storage.append(guesses)
    print("\n******************************")

    question_index += 1
    
    if  num_questions <= 3:
        num_questions += 1
            
    else: 
        print("GAME OVER!")
print("Play Again!")



"""
        guesses = input("Enter your answer (A, B, C, D): ").upper()
        #guesses.append(guesses_num)

        if guesses_num == answers[opt_index]:
            
            print("Next question!")
            break
        elif:
            print(f"Wrong answer!")
            guess -= 1
            print(f"{guess} left. Try again")
            guesses = input("Enter your answer (A, B, C, D): ").upper()
        else:
            guess == 0
            print("No more guesses!")
            break
    print("******************************")

        #if option == answers.len():
         #   print("Next question!")
    print("Wrong answer Try again!")
    print("******************************")

"""