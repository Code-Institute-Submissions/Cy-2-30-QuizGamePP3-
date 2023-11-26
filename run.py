import gspread
from google.oauth2.service_account import Credentials
#from colorama import Fore
import random
import methods

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

random_fact = random.choice(fun_facts)

print("Did you know!")
print("******************************")
print(random_fact)
print("******************************")

#change of game content filling missing words to multiple questions quiz
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

#random_word = random.choice(easy_words)
#print("Guess the words...")
#print(random_word)
"""

#Multiple questions quiz change from tuple to dictionaries 
"""
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

quiz_questions = {
    "question" : ["Where did the Christmas tree originate from? :", " What is the highest-grossing Christmas film of all time? :",
                "Where do Christmas gonks come from? :", "WIn what film would you hear the greeting 'Merry Christmas, ya filthy animal'? :", 
                "Before turkey, what was the traditional Christmas Day meal in England? :", "Which artist had the most Christmas No.1 singles? :", 
                "Who invented electric lights for the Christmas tree? :", "How much does the world's most expensive Christmas decoration cost? :", 
                "When did John Lewis open its online Christmas shop? :", "Where is the UK's tallest Christmas tree situated? :", 

                "Where is the oldest Christmas market in the world?  :", "What is a tree with fake snow called? :", 
                "How many gifts were given in total in 'The Twelve Days of Christmas' song?  :", "What color are mistletoe berries? :", 
                "What is the most popular Christmas plant in the UK? :", "How tall is the record holder for the tallest-ever snowman? :", 
                "How many Christmas puddings are sold in the UK on average? :", "Which country donates the Christmas tree in Trafalgar Square? :", 
                "Who invented the Christmas cracker? :", "Where does the name Boxing Day come from? :",

                "When was Christmas first celebrated in the UK? :", "How many tips do traditional snowflakes have? :", 
                "What is the most popular Christmas tree topper ornament? :", "According to UK traditions, when should Christmas decorations come down? :", 
                "Who started the tradition of exchanging gifts? :", "Where does the tradition of hanging gifts on the Christmas tree come from? :", 
                "Why do we give chocolate coins for Christmas? :", "Who wrote A Christmas Carol? :", 
                "What fruit is usually placed in stockings? :", "What was the Home Alone decor inspired by? :",

                "Who brought the Christmas tree to England? :", "Who invented the Christmas wreath? :", 
                "What is the most popular Christmas tree in the UK? :", "What was the first Christmas tree decoration? :", 
                "When do the 12 days (about 1 week 5 days) of Christmas start? :", "In which year was the first Christmas card sent? :", 
                "Where are the McCallisters going on holiday when they leave Kevin behind in Home Alone? :", "Stollen is the traditional fruit cake of which country? :", 
                "How many real Christmas trees are sold each year in the UK? :", "What is the name for the period between Christmas and New Year? :",

                "What country started the tradition of hanging stockings? :", "How many Christmas trees are grown in Europe each year? :", 
                "What does Holy represent? :", "When were electric Christmas tree lights invented? :", 
                "Before being developed into a toy, how did Elf on the Shelf begin? :", "Which accessory do you add to the base of your Christmas tree to hide the stand or trunk? :", 
                "When were turkeys first brought to England? :", "Aside from a fireplace mantel, where is the most popular place to use a Christmas garland in the home? :", 
                "Who designed the upside-down Christmas tree at Claridge's Hotel in 2017? :", "Which country invented glass baubles? :"
    ],

    "options" : [["Germany.", "Ireland.", "Canada."], ["Home Alone, raking in $300 million.", "The animated Dr Seuss' The Grinch 2018, raking in $512 million.", "Failure to Launch,raking in $100 million."], 
                ["United States.", "Soviet Union.", "Scandinavia."], ["Home Alone.", "Chrismas with Family.", "Two Half a Men"], 
                ["The traditional Christmas meal in England was rosted turkey.", "The traditional Christmas meal in England was a pig's head and mustard.", "The traditional Christmas meal in England was roasted ham."], ["The Beatles.", "Westlife.", "Boys to Men."], 
                ["Edward Johnson in the US in 1882.", "John Smith in the UK in 1750.", "Edward Dammes in Germany in 1950."], ["", "", "The emu egg set in 24-carat gold cost £8.9 million."], 
                ["31st July 2003.", "31st August 2023.", "31st December 2008."], ["", "", "Wakehurst, West Sussex."],

                ["Dresden's Striezelmarkt, Germany.", "Oslo street market, Norway.", "Dublin, chrismas market."], ["A pine tree.", "A flocked Christmas tree.", "Snowy Christmas tree."], 
                ["365.", "366.", "364."], ["White.", "Black.", "Yellow."], 
                ["Poinsettia.", "Chrismas lights.", "Mexican flame leaf."], ["200 feet.", "113 feet.", "213 feet."], 
                ["2 million.", "250 million.", "25 million."], ["Norway.", "France.", "Germany."], 
                ["Coonectcut-based confectioner Tom Waffles.", "Munich-based confectioner Gerhard Regards.", "London-based confectioner and baker Tom Smith."], ["Boxing Day was a traditional day off peace.", "Boxing Day was a traditional day off for servants in which they received a 'Christmas Box' from their master.", "Boxing Day was a traditional day off cleaning and resting after Chrismas Day."],

                ["In the 20th century.", "In the 6th century.", "In the 1th century."], ["Six.", "Seven.", "Nine."], 
                ["The devil.", "The ghost.", "An angel."], ["Twelfth Night, 5th or 6th January.", "Sixth Night, 15th or 16th January.", "twentyfirst Night, 28th or 29th January."], 
                ["The French.", "The Romans.", "The Rassians."], ["The Druids.", "The magicians.", "The Priest."], 
                ["To honor Saint Nicholas.", "To honor St Patrick.", "To honor Chrismas father."], ["Tom Hilfigure.", "Charles Dickens.", "Chulk Bass."], 
                ["An apple.", "An apricot.", "An orange."], ["Antique paintings.", "Antique cards and Norman Rockwell paintings.", "Chrismas cards."],

                ["Queen Charlotte, wife of King George III installed the first indoor tree (a yew tree) at Queen's Lodge, Windsor, in 1800 to mark the festive season", "Princess of Denmark, installed the first indoor tree at Queen's Lodge.", "Prince Albert, who, after importing several spruce firs from Germany in 1840, was credited with introducing the Christmas tree tradition to the masses."], ["An English Lutheran pastor named Jonh Rich.", "A Rassian Lutheran pastor named Piet Norman.", "A German Lutheran pastor named Johann Hinrich Wichern."], 
                ["Nordmann Smith.", "Nordmann Fir.", "John Norman."], ["Candles, introduced by Martin Luther in Germany.", "Candles, introduced by Martin Luther in USA.", "Candles, introduced by Martin Luther in England."], 
                ["25th December.", "24th December.", "26th December."], ["1850.", "1980.", "1843."], 
                ["Greese.", "Norway.", "France."], ["Poland.", "Germany.", "France."], 
                ["8 million.", "2 million.", "5 million."], ["Twixmas.", "Year end.", "31 celebration."],

                ["Norway.", "Greece.", "Italy."], ["60 million.", "200 million.", "66 million."], 
                ["Jesus Christ's cross.", "Jesus Christ's crown of thorns.", "Jesus Christ's cloth."], ["1850 by Edward Johnson in the US.", "1881 by Edward Johnson in the US.", "1882 by Edward Johnson in the US."], 
                ["Elf on the Shelf began as a children's picture book in 2005.", "Elf on the Shelf began as a children's picture book in 2006.", "Elf on the Shelf began as a children's picture book in 2007."], ["Tree skirt.", "Tree star.", "Tree lights."], 
                ["1950.", "1880.", "1526."], ["The stairs.", "Near the window.", "Next to the wood storage."], 
                ["Kelvin Cline.", "Tom Ford.", "Karl Lagerfeld."], ["Ireland.", "Germany.", "South America."]
    ],

    "answers" : ["Germany.", "The animated Dr Seuss' The Grinch (2018), raking in $512 million.", 
                "Scandinavia.", "Home Alone.", 
                "The traditional Christmas meal in England was a pig's head and mustard.", "The Beatles.", 
                "Edward Johnson in the US in 1882.", "The emu egg set in 24-carat gold cost £8.9 million.", 
                "31st August 2023.", "Wakehurst, West Sussex.", 

                "Dresden's Striezelmarkt, Germany.", ["A flocked Christmas tree.","Snowy Christmas tree."], 
                "364.", "White.", 
                "Poinsettia.", "113 feet.", 
                "25 million.", "Norway.", 
                "London-based confectioner and baker Tom Smith.", "Boxing Day was a traditional day off for servants in which they received a 'Christmas Box' from their master.",

                "In the 6th century.", "Six.", 
                "An angel.", "Twelfth Night, 5th or 6th January.", 
                "The Romans.", "The Druids.", 
                "To honor Saint Nicholas.", "Charles Dickens.", 
                "An orange.", "Antique cards and Norman Rockwell paintings.",

                ["Queen Charlotte, wife of King George III, installed the first indoor tree (a yew tree) at Queen's Lodge, Windsor, in 1800 to mark the festive season","Prince Albert, who, after importing several spruce firs from Germany in 1840, was credited with introducing the Christmas tree tradition to the masses."], "A German Lutheran pastor named Johann Hinrich Wichern.", 
                "Nordmann Fir.", "Candles, introduced by Martin Luther in Germany.", 
                "25th December.", "1843.", 
                "France.", "Germany.", 
                "8 million.", "Twixmas.", 

                "Italy.", "60 million.", 
                "Jesus Christ's crown of thorns.", "1882 by Edward Johnson in the US.", 
                "Elf on the Shelf began as a children's picture book in 2005.", "Tree skirt.", 
                "1526.", "The stairs.", 
                "Karl Lagerfeld.", "Germany.", 
    ]
}

random_word = random.choice(key.question)
print("Guess the words...")
print(random_word)

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


#example for the quiz
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